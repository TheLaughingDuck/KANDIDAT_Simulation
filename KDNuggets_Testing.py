import matplotlib.pyplot as plt

import random

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


n_samples = 250 # *Total* number of data points
n_features = 2 # No. of *variables*
n_clusters = 4
random_state = random.randint(1,100) #Seed for dataset creation. original: 42
max_iter = 100

X, y = make_blobs(n_samples=n_samples, 
                  n_features=n_features, 
                  centers=n_clusters)

print(type(X))

fig=plt.figure(figsize=(8,8), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(X[:, 0], X[:, 1])

plt.show()