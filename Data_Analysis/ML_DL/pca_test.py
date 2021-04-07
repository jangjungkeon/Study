# 특성공학 중 특성 추출(Feature Extraction)
# 특성을 단순히 선택하는 것이 아니라 특성들의 조합으로 새로운 특성을 생성 : PCA(주성분 분석)는 특성 추출 기법에 속함
# iris dataset 으로 차원 축소(4개의 열을 2개(sepal, petal))

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
plt.rc('font', family='NanumBarunGothic')

iris = load_iris()
n = 10
print(iris.data)
x = iris.data[:n, :2]           # sepal 자료로 패턴
print('차원 축소 전 x : \n', x, x.shape, type(x))        # [[5.1 3.5] ... (10, 2) <class 'numpy.ndarray'>
print(x.T)              # [5.1 4.9 4.7 4.6 5.  5.4 4.6 5.  4.4 4.9] ...

# 시각화
# plt.plot(x.T, 'o:')
# plt.xticks(range(2), ['꽃받침 길이', '꽃받침 폭'])
# plt.xlim(-0.5, 2)
# plt.ylim(2.5, 6)
# plt.title('iris 특성')
# plt.legend(['표본 {}'.format(i + 1) for i in range(n)])
# plt.show()


# 시각화2
ax = sns.scatterplot(0, 1, data=pd.DataFrame(x), markers='s', s=100, color='.2')
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))

plt.xlabel('꽃받침 길')
plt.ylabel('꽃받침 폭')
plt.title('iris 특성')
plt.show()

# PCA
pca1 = PCA(n_components=1)
x_row = pca1.fit_transform(x)       # 1차원 근사 데이터를 반환
print(x_row, x_row.shape)

x2 = pca1.inverse_transform(x_row)
print('복귀 후 값: \n', x2, x2.shape)
print(x_row[0])
print(x2[0, :])

# 시각화2 : 산포도 - 사영
ax = sns.scatterplot(0, 1, data=pd.DataFrame(x), markers='s', s=100, color='.2')
for i in range(n):
    d = 0.03 if x[i, 1] > x2[i, 1] else -0.04
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))
    plt.plot([x[i, 0], x2[i, 0]], [x[i, 1], x2[i, 1]], 'k--')

plt.plot(x2[:, 0], x2[:, 1], "o-", color='b', markersize=10)        # 추세선 추가
plt.plot(x[:, 0].mean(), x[:, 1].mean(), markersize=10, marker="D")
plt.axvline(x[:, 0].mean(), c='r')           # 세로선 추가
plt.axhline(x[:, 1].mean(), c='r')           # 가로선 추가
plt.xlabel('꽃받침 길')
plt.ylabel('꽃받침 폭')
plt.title('iris 특성')
plt.show()


print('***' * 10)
x = iris.data
pca2 = PCA(n_components=2)
x_row2 = pca2.fit_transform(x)
print("x_row2 : ", x_row2, x_row2.shape)

x4 = pca2.inverse_transform(x_row2)
print('최초자료 : ', x[0])
print('차원축소 : ', x_row2[0])
print('최초복귀 : ', x4[0, :])

print()
iris2 = pd.DataFrame(x_row2, columns=['sepal', 'petal'])
iris1 = pd.DataFrame(x, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(iris2.head(3))        # 차원 축소
print()
print(iris1.head(3))        # 원래 데이터























