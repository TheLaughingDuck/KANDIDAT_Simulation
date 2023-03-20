import kmeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random_data_testing_specific
import math
import random

### FIGURE 2
if False:
    # Simple demonstration of k-means
    seeds_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(1,5,7))

    # Run k-means
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


### Figure 5: Elbow method
if False:
    # Does not work, do not understand why
    data_fig5 = np.loadtxt("Data/UCI_data/seeds_dataset.txt", delimiter="\t", usecols=(2,4))
    kmeans.elbow_func(data_fig5, "random", 1, 5)


### Figure 9
if False:
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


### FIGURE 10
if False:
    
    K_values = [4,5,6,7,8,9]
    time_data_unifr    = [ 1.90,  5.6,  16.44, 49.1, 136.18, 351.84]
    time_data_plusplus = [ 0.12,  0.16,  0.16,  0.18,  0.21,   0.23]
    time_data_kaufman  = [19.81, 31.48, 51.3,  62.59, 88.58,  98.01]

    plt.plot(K_values, time_data_unifr, "g.", markersize=10, linestyle="dashed")
    plt.plot(K_values, time_data_plusplus, "k^", markersize=8, linestyle="dashed")
    plt.plot(K_values, time_data_kaufman, "m*", markersize=10, linestyle="dashed")

    plt.grid()

    plt.xlabel("Clusters (K)")
    plt.ylabel("Time (seconds)")

    plt.legend(["R-Batched UnifRandom", "K-means++", "Kaufman"])
    plt.show()


### Figure 3
if False:
    data_points = 500
    # Generate data
    #cluster_1 = random_data.make_clusters(N=10, d=2, K=1, plot_yesno = False, save_data = False, length=100, standard_dev=1)
    #cluster_2 = random_data.make_clusters(N=10, d=2, K=1, plot_yesno = False, save_data = False, length=100, standard_dev=10)
    data = random_data_testing_specific.make_clusters(data_points)

    # Plot data
    # Example
    # Simple demonstration of k-means
    #seeds_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(1,5,7))

    # Run k-means
    k_object = kmeans.kmeans_func(data, seed_method="plusplus", K=2, nstarts=2, table_output=False, plot_yesno=False, true_labels_included=False)
    # k_object = [best_centers, corresponding seed, CPU time (sec)]

    ### DETERMINE CLOSEST CLUSTER
    # Add column to data
    zero_column = np.array([[0] for i in range(data_points)])
    data = np.append(data, zero_column, axis=1)

    # Determine closest center
    data_no_belonging = np.delete(data, obj=2, axis=1)
    for i in range(len(data)):
        #print("data[i]", data_no_belonging[i])
        #print("k_object[0][0]", k_object[0][0])
        distance_to_c0 = math.dist(data_no_belonging[i], k_object[0][0])
        distance_to_c1 = math.dist(data_no_belonging[i], k_object[0][1])
        
        if distance_to_c0 < distance_to_c1:
            data[i][2] = 0
        else:
            data[i][2] = 1


    ## Create plot
    # Create colored scatterplot of the data
    plt.scatter(data[:,0], data[:,1], c=pd.factorize(data[:,2])[0], s=[20 for i in range(len(data))])

    # Add in the k-means-seed-points
    #plt.scatter(k_object[1][:,0], k_object[1][:,1], color="red", marker=".", s=130)

    # Add in k-means final centers
    plt.scatter(k_object[0][:,0], k_object[0][:,1], color="red", marker="*", s=130) #orange?

    # Add stylistic stuff
    #plt.xlabel("Perimeter")
    #plt.ylabel("Asymmetry coefficient")

    plt.show()


### Potatoes and Carrots plot
# Was never completed
if True:
    ## Create data
    # Generate TRUE centers
    true_centers = np.array([[25,250], [60, 95]])

    ## Store center belonging
    #center_belonging = []

    #one_point = random.choices(true_centers)[0]
    one_point = true_centers[0]

    # Store first points belonging
    #center_belonging.append(np.where(true_centers == one_point)[0][0])
    
    # standard deviation std
    std = 9

    randomness = [random.gauss(0, std) for i in range(2)] #array of gaussians
    data = np.array([one_point + randomness])

    # Create cluster 1
    while len(data) < 50:
        ### Select first center
        one_point = true_centers[0]
        #print("one_point", one_point)

        randomness = [random.gauss(0, std) for i in range(2)] #array

        one_point = one_point + randomness

        data = np.append(data, [one_point], axis=0)

    ## Plot cluster 1
    plt.scatter(data[:,0], data[:,1], c="Orange")

    ## Clear data
    one_point = true_centers[1]
    randomness = [random.gauss(0, std) for i in range(2)] #array of gaussians
    data = np.array([one_point + randomness])

    # Create cluster 2
    while len(data) < 50:
        ### Select second center
        one_point = true_centers[1]

        # Store center belonging
        #center_belonging.append(np.where(true_centers == one_point)[0][0])

        randomness = [random.gauss(0, std) for i in range(2)] #array

        one_point = one_point + randomness

        data = np.append(data, [one_point], axis=0)

    ## Plot cluster 2
    plt.scatter(data[:,0], data[:,1], c="Yellow")

    # Add stylistic stuff
    plt.xlabel("Width (mm)")
    plt.ylabel("Length (mm)")

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