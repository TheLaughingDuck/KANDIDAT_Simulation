import random_data
import kmeans
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.markers import MarkerStyle


### FIGURE 2
if False:
    # Simple demonstration of k-means
    seeds_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(1,5,7))

    # Runk k-means
    k_object = kmeans.kmeans_func(seeds_data, seed_method="plusplus", K=3, nstarts=10, table_output=False, plot_yesno=False, true_labels_included=True)
    # k_object = [best_centers, corresponding seed, CPU time (sec)]

    ## Create plot
    # Create colored scatterplot of the data
    plt.scatter(seeds_data[:,0], seeds_data[:,1], c=pd.factorize(seeds_data[:,2])[0], s=[20 for i in range(len(seeds_data))])

    # Add in the k-means-seed-points
    plt.scatter(k_object[1][:,0], k_object[1][:,1], color="red", marker=".", s=130)

    # Add in k-means final centers
    plt.scatter(k_object[0][:,0], k_object[0][:,1], color="orange", marker="X", s=130) #orange?

    # Add stylistic stuff
    plt.xlabel("Perimeter")
    plt.ylabel("Asymmetry coefficient")

    plt.show()



### Figure 9
if True:
    data = random_data.make_clusters(N=500, d=2, K=10, length=100)
    plt.scatter(data[:,0], data[:,1])

    # Plot UnifRandom initialization
    k_object_unifr = kmeans.kmeans_func(data, seed_method="random", K=10, nstarts=1, plot_yesno=False)
    plt.scatter(k_object_unifr[0][:,0], k_object_unifr[0][:,1], color="red", marker="D")
    
    # Plot k-mean++ initialization
    k_object_unifr = kmeans.kmeans_func(data, seed_method="plusplus", K=10, nstarts=1, plot_yesno=False)
    plt.scatter(k_object_unifr[0][:,0], k_object_unifr[0][:,1], color="orange", marker="*")

    # Plot kaufman initialization
    k_object_unifr = kmeans.kmeans_func(data, seed_method="kaufman", K=10, nstarts=1, plot_yesno=False)
    plt.scatter(k_object_unifr[0][:,0], k_object_unifr[0][:,1], color="green", marker="x")

    plt.show()





#df = pd.DataFrame(seeds_data)
#g = pd.plotting.scatter_matrix(df.drop(columns=[7]), c=pd.factorize(df[7])[0]) #Drop the category column
#plt.show()

# Run k-means and show plot of one of the scatterplots
#small_seed = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(1,5,7))
#object = kmeans.kmeans_func(small_seed, seed_method="plusplus", K=3, nstarts=1, table_output=False, plot_yesno=False, true_labels_included=True)


# IRIS
#iris_data = np.loadtxt("Data/iris.txt", delimiter=",")
#df_iris = pd.DataFrame(iris_data)
#print(df_iris.iloc[: , -1:])
#print(type(df_iris.iloc[: , -1:]))
#g_iris = pd.plotting.scatter_matrix(df_iris.iloc[: , :-1], c=pd.factorize(df_iris[4])[0])
#plt.show()