import numpy as np
import kmeans
import random_data

# All iris attributes are interesting
iris_data = np.loadtxt("Data/iris.txt", delimiter=",", usecols=(0,1,2,3))


# Seeds (the last column indicates type. There are 3 types/clusters)
seed_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(0,1,2,3,4,5,6))

# 10 groups?
wine_red_data = np.loadtxt("Data/winequality-red.csv", delimiter=";", skiprows=1)
wine_white_data = np.loadtxt("Data/winequality-white.csv", delimiter=";", skiprows=1)

#print(seed_data[:5])


### Elbow tests

#kmeans.elbow_func(seed_data, seed_method="plusplus", min_k=1, max_k=6)

#data = random_data.make_clusters(1000, d=2, K=6)

#kmeans.elbow_func(data, seed_method="plusplus", min_k=1, max_k=10)