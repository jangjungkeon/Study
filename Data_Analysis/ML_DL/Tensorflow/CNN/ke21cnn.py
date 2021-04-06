# MNIST 로 CNN 연습
import tensorflow as tf
from tensorflow.keras import datasets, models, layers

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
print(train_images.shape)

# CNN : 3차원을 4차원으로 구조 변경(채널 추가)
train_images = train_images.reshape((60000, 28, 28, 1))
print(train_images.shape, train_images.ndim)
train_images = train_images / 255.0
# print(train_images[0])
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images / 255.0
print(train_labels[:3])

# 모델
input_shape = (28, 28, 1)

model = models.Sequential()
#    형식 : filters, kernel_size, strides=(1, 1), padding='valid', ...
# padding='valid(0안씀)' or 'same(0씀)'
model.add(layers.Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu', input_shape=input_shape))
model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=None))      # None은 strides=(2, 2) 와 동일
model.add(layers.Dropout(0.2))
# 위의 3줄이 한팀임.

model.add(layers.Conv2D(32, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=None))      # None은 strides=(2, 2) 와 동일
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(16, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=None))      # None은 strides=(2, 2) 와 동일
model.add(layers.Dropout(0.2))

model.add(layers.Flatten())     # Fully connected layer - CNN 처리된 데이터를 1차원 자료로 변경
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

print(model.summary())
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping
earlyStop = EarlyStopping(patience=3, monitor='val_loss')
history = model.fit(train_images, train_labels,
                    batch_size=128, epochs=100, verbose=1, validation_split=0.2, callbacks=[earlyStop])


# 모델 저장
model.save('ke21cnn_10.hdf5')


import pickle
#history = history.history
#with open('data.pickle', 'wb') as f:
#    pickle.dump(history, f)


with open('data.pickle', 'rb') as f:
    history = pickle.load(f)

model = tf.keras.models.load_model('ke21cnn_10.hdf5')

# train_loss, train_acc = model.evaluate(train_images, train_labels)
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('train_loss : ', train_loss)
# print('train_acc : ', train_acc)
# print('test_loss : ', test_loss)
# print('test_acc : ', test_acc)

import numpy as np
print('예측값 : ', np.argmax(model.predict(test_images[:1])))
print('예측값 : ', np.argmax(model.predict(test_images[[0]])))
print('실제값 : ', test_labels[0])

print('예측값 : ', np.argmax(model.predict(test_images[[1]])))
print('실제값 : ', test_labels[1])

# acc 와 loss 로 시각화

import matplotlib.pyplot as plt
def plot_acc(title=None):
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    if title is not None:
        plt.title(title)
    plt.ylabel(title)
    plt.xlabel('epoch')
    plt.legend(['train data', 'validation data'], loc=0)


plot_acc('accuracy')
plt.show()


def plot_loss(title=None):
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    if title is not None:
        plt.title(title)
    plt.ylabel(title)
    plt.xlabel('epoch')
    plt.legend(['train data', 'validation data'], loc=0)


plot_loss('loss')
plt.show()
