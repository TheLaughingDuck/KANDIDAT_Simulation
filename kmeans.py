from sklearn.cluster import KMeans
import seeds


'''Program file for running the k-means algorithm.'''


def kmeans(data, seed_method, K, nstarts=1):

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

        # We still have to compare the load/cost/weight of each run.
    
    
    return kmeans_object.cluster_centers_
