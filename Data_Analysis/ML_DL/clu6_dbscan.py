# 밀도 기반 클러스터링 : Kmeans와 달리 K를 지정하지 않음.
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

x, y = make_moons(n_samples=200, noise=0.05, random_state=0)
print(x)
print(y)

plt.scatter(x[:, 0], x[:, 1])
plt.show()

# KMeans 사용 : 완전한 분리 X
km = KMeans(n_clusters=2, random_state=0)
pred1 = km.fit_predict(x)


def plotResult(x, y):
    plt.scatter(x[y == 0, 0], x[y == 0, 1], c='blue', marker='o', label='clu-1')
    plt.scatter(x[y == 1, 0], x[y == 1, 1], c='red', marker='s', label='clu-2')
    plt.legend()
    plt.show()


plotResult(x, pred1)

print()
# DBSCAN 사용
dm = DBSCAN(eps=0.2, min_samples=5, metric="euclidean")
pred2 = dm.fit_predict(x)
print(pred2)
plotResult(x, pred2)


























































































































