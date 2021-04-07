# 모델 학습 시 k-fold 교차 검증 : train data에 대해 k겹으로 나눠서 검증
# k-fold 교차 검증을 할 떄는 validation_split을 사용하지 않는다.
# 데이터의 양이 적을 경우 많이 사용되는 방법.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score
from tensorflow.python.keras.wrappers.scikit_learn import KerasClassifier

data = np.loadtxt('https://raw.githubusercontent.com/jangjungkeon/Study/main/Data/dataset/diabetes.csv',
                  dtype=np.float32, delimiter=',')
print(data, data.shape)     # (759, 9)

x = data[:, 0:-1]
y = data[:, -1]
print(x[:2])
print(y[:2])

# 일반적인 모델 네트워크
model = Sequential([
    Dense(units=64, input_dim=8, activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=1, activation='sigmoid'),
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])
model.fit(x, y, epochs=200, batch_size=32, verbose=2)
print(model.evaluate(x, y))

print()
def build_model():
    model = Sequential()
    model.add(Dense(units=64, input_dim=8, activation='relu'))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
# k-fold 교차검증 모델 네트워크


estimatorModel = KerasClassifier(build_fn=build_model, epochs=200, batch_size=32, verbose=2)
kfold = KFold(n_splits=5, shuffle=True, random_state=12)
print(cross_val_score(estimatorModel, x, y, cv=kfold))
estimatorModel.fit(x, y, epochs=200, batch_size=32, verbose=2)
# print(estimatorModel.evaluate(x, y))

pred = estimatorModel.predict(x[:3, :])
print('예측값 : ', pred.flatten())
print('실제값 : ', y[:3])

print()
from sklearn.metrics import accuracy_score
print('분류정확도(estimatorModel)', accuracy_score(y, estimatorModel.predict(x)))
