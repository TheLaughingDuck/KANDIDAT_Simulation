import numpy as np
import random_data
import kmeans
import seeds

#seed_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(0,1,2,3,4,5,6,7))

#plus_seed_test = kmeans.kmeans_func(seed_data, seed_method="plusplus", K=3, nstarts=10, table_output=True, true_labels_included=True)

# All iris attributes are interesting. K=3
#iris_data = np.loadtxt("Data/iris.txt", delimiter=",", usecols=(0,1,2,3,4))

#plus_iris_test = kmeans.kmeans_func(iris_data, seed_method="plusplus", K=3, nstarts=10, table_output=True, true_labels_included=True)
#print(plus_iris_test)


#test_data = np.loadtxt("Data/testmakeclusters.txt", delimiter=",")

#plus_test_test = kmeans.kmeans_func(test_data, seed_method="plusplus", K=4, nstarts=10, table_output=True, true_labels_included=True)

#print(plus_test_test)



test1_data = np.loadtxt("Data/iris.txt", delimiter=",")
test1 = kmeans.kmeans_func(test1_data, seed_method="random", K=3, nstarts=1, table_output=True, true_labels_included=True)
print("Performing test iris: K=3, s=1")
print(test1)
print("-----------------------------")

test2_data = np.loadtxt("Data/iris.txt", delimiter=",")
test2 = kmeans.kmeans_func(test2_data, seed_method="random", K=3, nstarts=12, table_output=True, true_labels_included=True)
print("Performing test iris (s): K=3, s=12")
print(test2)
print("-----------------------------")