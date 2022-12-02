from sklearn.cluster import KMeans
import seeds
import math


'''Program file for running the k-means algorithm.'''


def kmeans_func(data, seed_method, K, nstarts=1):
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
    
    return best_centers
