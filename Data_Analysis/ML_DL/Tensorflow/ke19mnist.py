# 숫자 이미지(MNIST) dataset으로 image 분류 모델

import tensorflow as tf
import sys
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(len(x_train), len(y_train), len(x_test), len(y_test))
print(type(x_train))
print(x_train.shape, y_train.shape)     # (60000, 28, 28) (60000, )
print(x_train[0])

x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')

# for i in x_train[0]:
#     for j in i:
#         sys.stdout.write('%s ' % j)
#     sys.stdout.write('\n')
print(y_train[0])

x_train /= 255          # 0 ~ 255 사이의 값을 0 ~ 1 사이로 정규화
x_test /= 255
print(x_train[0])
# plt.imshow(x_train[0], cmap='Greys')
# plt.show()

print(y_train[0])
print(set(y_train))

y_train = tf.keras.utils.to_categorical(y_train, 10)        # one-hot
y_test = tf.keras.utils.to_categorical(y_test, 10)
print(y_train[0])

# train dataset 의 일부를 validation dataset
x_val = x_train[50000:60000]
y_val = y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
print(x_val.shape, ' ', x_train.shape)      # (10000, 28, 28)       (50000, 28, 28)

model = tf.keras.Sequential()
# 784 = 28 * 28
model.add(tf.keras.layers.Dense(512, input_shape=(784, )))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(512))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(512, kernel_regularizer=tf.keras.regularizers.l2(0.001)))     # 가중치 규제
model.add(tf.keras.layers.Dense(512))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

# 훈련
from tensorflow.keras.callbacks import EarlyStopping
e_stop = EarlyStopping(patience=5, monitor='loss')
history = model.fit(x_train, y_train, epochs=1000, batch_size=256, validation_data=(x_val, y_val),
                    verbose=1, callbacks=[e_stop])
print(history.history.keys())

print('loss : ', history.history['loss'], ', val_loss : ', history.history['val_loss'])
print('acc : ', history.history['accuracy'], ', val_acc : ', history.history['val_accuracy'])

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

score = model.evaluate(x_test, y_test)
print(score)
print('score loss : ', score[0])
print('score acc : ', score[1])

model.save('ke19mnist_1000_256.hdf5')
model = tf.keras.models.load_model('ke19mnist_1000_256.hdf5')

# 예측
pred = model.predict(x_test[:1])
print('예측값 : ', pred)


import numpy as np
print('예측값 : ', np.argmax(pred))
print('실제값 : ', y_test[:1])
print('실제값 : ', np.argmax(y_test[:1], 1))

print('------------------')
from PIL import Image

im = Image.open('num1.png')
img = np.array(im.resize((28, 28), Image.ANTIALIAS).convert('L'))
print(img, img.shape)

data = img.reshape([1, 784])
data = data / 255
print(data)

new_pred = model.predict(data)
print('new_pred : ', new_pred)
print(np.argmax(new_pred, 1))



