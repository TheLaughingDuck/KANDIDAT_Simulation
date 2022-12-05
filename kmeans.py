from sklearn.cluster import KMeans
import seeds
import math


'''Program file for running the k-means algorithm.'''


def kmeans_func(data, seed_method, K, nstarts=1, plot_yesno=True):
    '''
    Returns a list: [best_centers, loss_list]
    best_centers is an array of the best centers.
    loss_list is a list of length nstarts containing the SumSqrErr (SSE) for each start.
    '''

    # list of loss values calculated for every start.
    loss_list = []
    
    # list of "finished" centres after every start.
    finished_centers = []

    for i in range(nstarts):
        #Run one iteration of the algorithm

        # Run the appropriate seed method
        if seed_method == "random":
            seed = seeds.random_seed(data, K)
        elif seed_method == "plusplus":
            seed = seeds.plusplus(data, K)
        elif seed_method == "kaufman":
            seed = seeds.kaufman(data, K)
        else:
            raise Exception("Bad seed_method input. Use one of \{\"random\", \"plusplus\", \"kaufman\"\}")
    
        kmeans_object = KMeans(n_clusters = K, init=seed, n_init=1, max_iter=100).fit(data)
        centers = kmeans_object.cluster_centers_

        ### Calculate load/loss/cost/weight

        # list of cluster-association index
        index_list = []

        # list of closest distance
        shortest_D_list = []
        
        # Assign all points to their closest cluster (keep track using index).
        for i in range(len(data)):
            shortest_D = None
            center_index = None
            for j in range(len(seed)):
                # Calculate D-istance
                D = math.dist(data[i], seed[j])

                if shortest_D == None:
                    shortest_D = D
                elif D < shortest_D:
                    shortest_D = D
                    center_index = j
            # Keep track of closest index and distance
            index_list.append(j)
            shortest_D_list.append(shortest_D)
        
        # Calculate cost
        COST = sum([i**2 for i in shortest_D_list])

        loss_list.append(COST)
        finished_centers.append(centers)
    
    ### Select the set of centers with lowest associated COST
    best_centers = finished_centers[loss_list.index(min(loss_list))]

    ### Possibly make a plot?
    if len(data[0]) == 2 and nstarts == 1 and plot_yesno == True:
        make_plot(data, seed, best_centers)
    
    return [best_centers, loss_list]

import matplotlib.pyplot as plt


def make_plot(data, seed, centers):
    #Plot data
    plt.scatter(data[:,0], data[:,1], marker=".")
    
    #Plot seed
    plt.scatter(seed[:,0], seed[:,1], color="red", marker=".")

    #Plot final centers
    plt.scatter(centers[:,0], centers[:,1], color="orange", marker="*")

    #Label fix
    plt.figtext(x=0.5, y=0.01, s="Text here", wrap=True)

    # Show plot
    plt.show()



def elbow_func(data, seed_method, min_k=1, max_k=10):
    k_values = [i for i in range(min_k, max_k+1)]
    Cost_list = []
    for i in k_values:
        # Run k-means and grab the loss_list (at pos 1), and take its mean.
        kmeans_avg_loss = sum(kmeans_func(data, seed_method=seed_method, K=i, nstarts=10, plot_yesno=False)[1])/10
        Cost_list.append(kmeans_avg_loss)
    
    # Plot Elbow graph
    plt.scatter(k_values, Cost_list)

    # Show
    plt.show()