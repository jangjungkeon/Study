# RandomForest, DecisionTree : 정량적인 분석 모델

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

boston = load_boston()          # array로 넘어옴
print(boston.DESCR)
dfx = pd.DataFrame(boston.data, columns=boston.feature_names)       # dataFrame으로 변환해주어야
dfy = pd.DataFrame(boston.target, columns=['MEDV'])
print(dfx.head(3), dfx.shape)
print(dfy.head(3))
df = pd.concat([dfx, dfy], axis=1)
print(df.head(2))
pd.set_option('display.max_columns', 100)
print(df.corr())


x = df[['LSTAT', 'TAX']].values
y = df['MEDV'].values
print(x[:2])
print(y[:2])

# 실습1
model = DecisionTreeRegressor(max_depth=3).fit(x, y)
print('predict : ', model.predict(x)[:5])
print('real : ', y[:5])

r2 = r2_score(y, model.predict(x))
print('결정계수(R2, 설명력) : ', r2)


# 실습2
model2 = RandomForestRegressor(n_estimators=1000, criterion='mse', random_state=123).fit(x, y)        # criterion='mse' 평균제곱오차
print('predict : ', model2.predict(x)[:5])
print('real : ', y[:5])

r2_1 = r2_score(y, model2.predict(x))
print('결정계수(R2_1, 설명력) : ', r2_1)

print('\n학습/검정 자료로 분리')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)
model2.fit(x_train, y_train)

r2_train = r2_score(y_train, model2.predict(x_train))       # train에 대한 설명력
print('train에 대한 설명력: ', r2_train)      # 0.909065

r2_test = r2_score(y_test, model2.predict(x_test))       # train에 대한 설명력
print('test에 대한 설명력: ', r2_test)        # 0.57796   독립변수의 수를 늘려주면 결과는 달라짐


# 시각화
# from matplotlib import style
# style.use('seaborn-talk')
# plt.scatter(x, y, c='lightgray', label='train data')
# plt.scatter(x_test, model2.predict(x_test), c='r', label='predict data')
# plt.xlabel('LSTA')
# plt.ylabel('MEDV')
# plt.legend()
# plt.show()

# # 새값으로 예측
# import numpy as np
# print(x_test[:3])
# x_new = [[50.11], [26.53], [1.76]]
# print("예상 집값 : ", model2.predict(x_new))





































































