# 회귀분석 모델 :
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.keras.applications.densenet import layers


dataset = pd.read_csv('https://raw.githubusercontent.com/jangjungkeon/Study/main/Data/dataset/auto-mpg.csv')
print(dataset.head(2))
del dataset['car name']
print(dataset.head(2))
pd.set_option('display.max_columns', 100)
print(dataset.corr())
dataset.drop(['cylinders', 'acceleration', 'model year', 'origin'], axis=1, inplace=True)
print()
print(dataset.head(2))
dataset['horsepower'] = dataset['horsepower'].apply(pd.to_numeric, errors="coerce")
print(dataset.isnull().sum())
print(dataset.info())
dataset = dataset.dropna()
print(dataset.isnull().sum())

import seaborn as sns
sns.pairplot(dataset[['mpg', 'displacement', 'horsepower', 'weight']], diag_kind='kde')
plt.show()


# train / test
train_dataset = dataset.sample(frac=0.7, random_state=123)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset.shape)
print(test_dataset.shape)

# 표준화 작업(수식을 직접 사용)을 위한 준비
train_stat = train_dataset.describe()
train_stat.pop('mpg')
train_stat = train_stat.transpose()
print(train_stat)

# label : mpg
train_labels = train_dataset.pop('mpg')
print(train_labels[:2])
test_labels = test_dataset.pop('mpg')
print(test_labels[:2])


def st_func(x):
    return (x - train_stat['mean']) / train_stat['std']


# print(st_func(10))
# print(train_dataset[:3])
# print(st_func(train_dataset[:3]))

st_train_data = st_func(train_dataset)      # train feature
st_test_data = st_func(test_dataset)        # test feature
# --------------- 모델에 적용할 dataset 준비 완료 휴우 ----------

# Model
def build_model():
    network = tf.keras.Sequential([
        layers.Dense(units=64, input_shape=[3], activation='linear'),
        layers.Dense(64, activation='linear'),
        layers.Dense(1, activation='linear'),
    ])
    # opti = tf.keras.optimizers.RMSprop(0.01)
    opti = tf.keras.optimizers.RMSprop(0.01)
    network.compile(optimizer=opti, loss='mean_squared_error',
                    metrics=['mean_absolute_error', 'mean_squared_error'])
    return network


print(build_model().summary())
model = build_model()
# fit() 전에 모델을 실행해 볼 수 도 있다.
print(model.predict(st_train_data[:1]))         # fitting 전에 결과를 낼 수는 있다.

# 훈련
epochs = 1000

# 학습 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
history = model.fit(
    st_train_data, train_labels, batch_size=32, epochs=epochs, validation_split=0.2, verbose=1,
    callbacks=[early_stop])
df = pd.DataFrame(history.history)
print(df.head(3))
print(df.columns)


# 시각화
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure(figsize=(8, 12))

    plt.subplot(2, 1, 1)
    plt.xlabel('epoch')
    plt.ylabel('Mean Abs Error[MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='train error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='val error')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.xlabel('epoch')
    plt.ylabel('Mean Squared Error[MPG]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='train error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='val error')
    plt.legend()
    plt.show()


plot_history(history)

