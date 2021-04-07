# 다중선형회귀모델 + 텐서보드 (모델의 구조 및 학습과정 / 결과를 시각화)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf


# 5명 세 번의 시험 점수로 다음 번 시험 점수 예측
x_data = np.array([[70, 85, 80], [71, 89, 78], [50, 80, 60], [66, 20, 60], [50, 30, 10]])
y_data = np.array([73, 82, 72, 57, 34])

print('Sequential API---------------------')
model = Sequential()
model.add(Dense(6, input_dim=3, activation='linear', name='a'))
model.add(Dense(3, activation='linear', name='b'))
model.add(Dense(1, activation='linear', name='c'))
print(model.summary())

opti = optimizers.Adam(lr=0.01)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model.fit(x_data, y_data, batch_size=1, epochs=30, verbose=2)

# plt.plot(history.history['loss'])
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.show()
loss_metrics = model.evaluate(x=x_data, y=y_data)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력: ', r2_score(y_data, model.predict(x_data)))

print('예측값 : ', model.predict(x_data).flatten())

print('function API ---------------')
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
inputs = Input(shape=(3, ))
output1 = Dense(6, activation='linear', name='a')(inputs)
output2 = Dense(3, activation='linear', name='b')(output1)
output3 = Dense(1, activation='linear', name='c')(output2)
linear_model = Model(inputs, output3)
print(linear_model.summary())


# TensorBoard : 알고리즘에 대한 동작을 확인. 시행착오를 최소화 가능.
from tensorflow.keras.callbacks import TensorBoard

tb = TensorBoard(log_dir='my',
                 histogram_freq=True,
                 write_graph=True,
                 write_images=False)


opti = optimizers.Adam(lr=0.01)
linear_model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = linear_model.fit(x_data, y_data, batch_size=1, epochs=30, verbose=2, callbacks=[tb])
print(history.history)

loss_metrics = linear_model.evaluate(x=x_data, y=y_data)
print('loss_metrics : ', loss_metrics)                                   # mse의 값을 의미. [30.13197898864746, 30.13197898864746]
print('설명력: ', r2_score(y_data, linear_model.predict(x_data)))          # 0.89369

# 새로운 값 예측
x_new = np.array([[50, 55, 50], [91, 99, 98]])
print('예상 점수 : ', linear_model.predict(x_new).flatten())














































































