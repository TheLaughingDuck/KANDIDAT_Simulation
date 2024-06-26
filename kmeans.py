from sklearn.cluster import KMeans
import seeds
import math
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode
import pandas as pd

from ttictoc import tic,toc

'''Program file for running the k-means algorithm.'''


def kmeans_func(data, seed_method, K, nstarts=1, plot_yesno=True, table_output=False, true_labels_included = False):
    '''
    Returns a list: [best_centers, final_loss_list]
    best_centers is an array of the best centers.
    final_loss_list is a list of length nstarts containing the SumSqrErr (SSE) for each start.
    '''

    data_with_labels = None
    if true_labels_included == True:
        data_with_labels = data
        #true_labels = data[:,-1]
        data = np.delete(data, obj=-1, axis=1) # Delete last column

    # Timing
    tic()

    # lists of loss at start, loss after k-means and required iterations.
    # All will have length nstarts
    start_loss_list = []
    final_loss_list = []
    requ_iterations = []
    label_list = []
    seed_list = []
    
    
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

        seed_list.append(seed)

        ## RUN k-means Algorithm
        kmeans_object = KMeans(n_clusters = K, init=seed, n_init=1, max_iter=100).fit(data)
        centers = kmeans_object.cluster_centers_

        label_list.append(kmeans_object.labels_)

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
        make_plot(data, seed, best_centers, data_with_labels)
    
    ### TABLE OUTPUT
    # Output *min SSE*, *% SSE decrease*, *avg required iterations*
    if table_output == True:
        print("K-means ouput:")
        print("[accuracy (%), final_loss, seed_loss, CPU_time (s), avg_iter]")
        return format_output(start_loss_list, final_loss_list, requ_iterations, nstarts, data_with_labels, label_list, true_labels_included)
    
    ### NORMAL OUTPUT
    print("K-means output:")
    print("[best_centers, corresponding seed, CPU time (sec)]")
    resulting_seed = seed_list[final_loss_list.index(min(final_loss_list))]
    return [best_centers, resulting_seed, toc()]



def format_output(start_loss_list, final_loss_list, iterations, nstarts, data_with_labels, label_list, true_labels_included):
    min_loss = min(final_loss_list)
    
    index = final_loss_list.index(min_loss)

    seed_SSE = start_loss_list[index]
        
    avg_iter = sum(iterations)/nstarts

    computation_time = toc()

    if true_labels_included == False:
        accuracy = 0
        print("Error: data_with_labels = None")
    else:
        accuracy = accuracy_func(data_with_labels, label_list[index]) # Returns a percentage

    # Build output, fix rounding and throw on units
    #OUTPUT = [min_loss, seed_SSE, avg_iter, computation_time, accuracy]
    OUTPUT = [accuracy, min_loss, seed_SSE, computation_time, avg_iter]
    OUTPUT = [round(i, 2) for i in OUTPUT]
    UNITS = [" %", "", "", " sec", " iterations"]

    return [str(OUTPUT[i]) + UNITS[i] for i in range(5)]


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



def make_plot(data, seed, centers, data_with_labels):
    #Plot data
    #print(type(data_with_labels))
    if data_with_labels is not None:
        plt.scatter(data[:,0], data[:,1], marker=".", c=pd.factorize(data_with_labels[:,2])[0])
    else: #data_with_labels is None
        plt.scatter(data[:,0], data[:,1], marker=".")
    
    #Plot seed
    plt.scatter(seed[:,0], seed[:,1], color="red", marker=".")

    #Plot final centers
    plt.scatter(centers[:,0], centers[:,1], color="orange", marker="*")

    #Label fix
    #plt.figtext(x=0.5, y=0.01, s="Text here", wrap=True)

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



def accuracy_func(arr, model_assignment):
    '''
    data: numpy array, with the last column containing *true* labels (coded by integers).

    model_assignment: numpy array, with the *assigned* labels (coded by integers) from the kmeans algorithm.

    Clearly it is assumed that model_assignment is based on the same ordering as in data.
    '''
    #print("arr:\n", arr)

    #print("model_assignment:\n", model_assignment)

    # Get true labels
    true_labels = np.unique(arr[:,-1], axis=0) # Array of unique elements in true label column (last column)

    # Array copy we can manipulate (also attaching kmeans assignment as column on the right)
    remaining_data = np.append(arr, [[i] for i in model_assignment], axis=1)

    correctly_assigned = 0 # Count
    for i in true_labels:
        #print("i:\n", i)
        #print("Begin label: ", i)
        one_cluster = remaining_data[remaining_data[:,-2] == i] # Creates array of all points in true cluster i
        #print("this_cluster:\n", one_cluster)

        # Find mode (in kmeans assignment)
        #print("one_cluster:\n", one_cluster)
        if len(one_cluster) != 0:
            the_mode = mode(one_cluster[:,-1]) # Grab mode of last column

            # Delete points belonging to the "assignment mode"
            remaining_data = np.delete(remaining_data, obj=remaining_data[:,-1] == the_mode, axis=0)
            #print("Remaining data:\n", remaining_data)

            numb_popular_index = list(one_cluster[:,-1]).count(the_mode)
        else:
            print("WARNING: I may have found an empty cluster with index i: ", i)
            print("The reason for this might be that your ratio of k to N is too large.")
            print("In other words, you have few enough clusters K for your N points, that it is possible this cluster was left empty when the dataset was created.")
            #However, I seem to have reasonably disproven this. My new theory is that
            # through this loop, points are assigned to varios clusters, and it just so happens that
            # the true clusters that cause this issue (len(one_cluster) is equal to 0) have had
            # all their points assigned to other kmeans-made clusters before they had a chance to
            # "claim" their own clusters in this accuracy calculation. THATS MY THEORY ANYWAY.
            # When bugtesting this, I used a dataset with N=1000, d=2, K=100
            
            numb_popular_index = 0
        #print("the mode: ", the_mode)


        #print("Adding: ", numb_popular_index)
        correctly_assigned += numb_popular_index
        #print("---------------------")

    #print("Correctly assigned: ", correctly_assigned/len(arr))
    
    return(round(100*correctly_assigned/len(arr), 2))