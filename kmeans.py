from sklearn.cluster import KMeans
import seeds
import math
import matplotlib.pyplot as plt

'''Program file for running the k-means algorithm.'''


def kmeans_func(data, seed_method, K, nstarts=1, plot_yesno=True, table_output=False):
    '''
    Returns a list: [best_centers, final_loss_list]
    best_centers is an array of the best centers.
    final_loss_list is a list of length nstarts containing the SumSqrErr (SSE) for each start.
    '''

    # lists of loss at start, loss after k-means and required iterations.
    # All have length nstarts
    start_loss_list = []
    final_loss_list = []
    requ_iterations = []
    
    
    # list of "finished" centres after every start.
    finished_centers = []

    iteration = 1
    while iteration <= nstarts:
    #for i in range(nstarts):
        ### RUN appropriate SEED METHOD
        if seed_method == "random":
            seed = seeds.random_seed(data, K)
        elif seed_method == "plusplus":
            seed = seeds.plusplus(data, K)
        elif seed_method == "kaufman":
            if nstarts != 1:
                print("PLEASE NOTE that the KAUFMAN seeding method is DETERMINISTIC.")
                print("Settings n_starts > 1 is therefore... maybe not \"idiotic\", but certainly superfluos.")
                print("I have thus changed nstarts to 1.")
                nstarts = 1
                #i = nstarts
            seed = seeds.kaufman(data, K)
        else:
            raise Exception("Bad seed_method input. Use one of \{\"random\", \"plusplus\", \"kaufman\"\}")

        ## Calculate start loss
        start_loss_list.append(calculate_cost(data, seed))

        ## RUN k-means Algorithm
        kmeans_object = KMeans(n_clusters = K, init=seed, n_init=1, max_iter=100).fit(data)
        centers = kmeans_object.cluster_centers_

        # Save number of iterations required
        requ_iterations.append(kmeans_object.n_iter_)
        
        ## Calculate final loss
        final_loss_list.append(calculate_cost(data, centers))
        finished_centers.append(centers)

        ## Next iteration
        iteration += 1
    
    ### Select the set of centers with lowest associated COST
    best_centers = finished_centers[final_loss_list.index(min(final_loss_list))]

    ### PRODUCE PLOT
    # Make scatterplot with data, seed and final centers if possible
    if len(data[0]) == 2 and plot_yesno == True:
        make_plot(data, seed, best_centers)
    
    ### TABLE OUTPUT
    # Output *min SSE*, *% SSE decrease*, *avg required iterations*
    if table_output == True:
        min_loss = min(final_loss_list)

        SSE_decrease = 100 * (min_loss / start_loss_list[final_loss_list.index(min_loss)]) #Percentage

        avg_iter = sum(requ_iterations)/nstarts

        return [round(min_loss, 5), round(SSE_decrease, 2), avg_iter]
    
    ### NORMAL OUTPUT
    return [best_centers, final_loss_list]




def calculate_cost(data, seed):
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
        shortest_D_list.append(shortest_D)
        
        # Calculate cost
    COST = sum([i**2 for i in shortest_D_list])

    return COST

    




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
        # Run k-means and grab the final_loss_list (at pos 1), and take its mean.
        kmeans_avg_loss = sum(kmeans_func(data, seed_method=seed_method, K=i, nstarts=10, plot_yesno=False)[1])/10
        Cost_list.append(kmeans_avg_loss)
    
    # Plot Elbow graph
    plt.scatter(k_values, Cost_list)

    # Show
    plt.show()