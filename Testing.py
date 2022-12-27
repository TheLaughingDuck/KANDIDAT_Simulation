import numpy as np
import random_data
import kmeans
import seeds
import matplotlib.pyplot as plt
import pandas as pd

#seed_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(0,1,2,3,4,5,6,7))

#plus_seed_test = kmeans.kmeans_func(seed_data, seed_method="plusplus", K=3, nstarts=10, table_output=True, true_labels_included=True)

# All iris attributes are interesting. K=3
#iris_data = np.loadtxt("Data/iris.txt", delimiter=",", usecols=(0,1,2,3,4))

#plus_iris_test = kmeans.kmeans_func(iris_data, seed_method="plusplus", K=3, nstarts=10, table_output=True, true_labels_included=True)
#print(plus_iris_test)


#test_data = np.loadtxt("Data/testmakeclusters.txt", delimiter=",")

#plus_test_test = kmeans.kmeans_func(test_data, seed_method="plusplus", K=4, nstarts=10, table_output=True, true_labels_included=True)

#print(plus_test_test)


### MAKE CLUSTERS
#random_data.make_clusters(N=1000, d=3, K=9, save_data=True, length = 1000)


### PERFORM COMPARATIVE TESTS
#print("Performing test: K=9, s=1, k-means++")
#test1_data = np.loadtxt("Data/Comparative_study/datak9.txt", delimiter=",")
#test1 = kmeans.kmeans_func(test1_data, seed_method="plusplus", K=9, nstarts=1, table_output=True, true_labels_included=True)
#print(test1)
#print("-----------------------------")



seeds_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(0,1,2,3,4,5,6,7))
plt.scatter(seeds_data[:,0], seeds_data[:,6], c=pd.factorize(seeds_data[:,7])[0])
plt.show()