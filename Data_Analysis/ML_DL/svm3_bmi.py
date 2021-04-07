# BMI의 계산방법 : 체중 / 신장**2
# print(73 / ((1.74)**2))


import random

def calc_bmi(h, w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5:
        return 'thin'
    if bmi < 23:
        return 'normal'
    return 'fat'


# print(calc_bmi(170, 65))

# 파일 만들기
# with open('bmi.csv', 'w') as f:
#     f.write('height,weight,label\n')
#     cnt = {'thin': 0, 'normal': 0, 'fat': 0}
#     for i in range(50000):
#         h = random.randint(150, 200)
#         w = random.randint(35, 100)
#         label = calc_bmi(h, w)
#         cnt[label] += 1
#         f.write(f'{h},{w},{label}\n')
#
# print(cnt)

# BMI dataset 으로 분류
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split        # train데이터와 test데이터를 나누는 모듈
import pandas as pd
import matplotlib.pyplot as plt

tbl = pd.read_csv('bmi.csv')

# 단위가 달라서 칼럼을 정규화 시키기.
label = tbl['label']
w = tbl['weight'] / 100
h = tbl['height'] / 200
wh = pd.concat([w, h], axis=1)
print(wh.head(5), wh.shape)         # (50000, 2)
print()
label = label.map({'thin': 0, 'normal': 1, 'fat': 2})
print(label[:5], label.shape)       # (50000, )

# train / test
data_train, data_test, label_train, label_test = train_test_split(wh, label)        # 문제, 답(label)
print(data_train.shape, data_test.shape)

# model
model = svm.SVC(C=0.01).fit(data_train, label_train)          # 문제, 답(label)
# model = svm.LinearSVC().fit(data_train, label_train)
# print(model)
# 학습한 데이터의 결과가 신뢰성이 있는지 확인하기 위해 교차검증 ----
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, wh, label, cv=3)
print('각각의 검증 결과: ', cross_vali)
print('평균 검증 결과: ', cross_vali.mean())
# -----------------------------------------------

pred = model.predict(data_test)
ac_score = metrics.accuracy_score(label_test, pred)
print('분류 정확도: ', ac_score)
print(metrics.classification_report(label_test, pred))

tbl2 = pd.read_csv('bmi.csv', index_col=2)
print(tbl2[:3])


# 시각화
def scatter_func(lbl, color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label=lbl)


scatter_func('fat', 'red')
scatter_func('normal', 'yellow')
scatter_func('thin', 'blue')
plt.legend()
plt.savefig('bmi_test50000.png')
plt.show()



























