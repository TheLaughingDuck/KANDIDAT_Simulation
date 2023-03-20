import random
import numpy as np
import matplotlib.pyplot as plt


# Large "blank dataframe" N rows, d+1 columns.
# The extra column is reserved for "true" cluster affiliation.
#pd.DataFrame([[0 for i in range(d)]+[1] for j in range(N)] , columns=[k for k in range(0,d+1)])



def make_clusters(N, plot_yesno = False, save_data = False, length=20):
    d=2
    K=2

    if N % 2 != 0:
        N += 1


    if save_data == True:
        print("-----------------------")
        print("You have opted to save the cluster data in a file.")
        print("Please input filename. No file extension (.txt is automatically added)")
        filename = input(">>")

    ### Generate TRUE centers
    #true_centers = np.array([[25,250], [60, 95]]) # Potatoes and carrots
    true_centers = np.array([[random.random()*length for i in range(d)] for i in range(K)])

    ## Store center belonging
    center_belonging = []

    one_point = random.choices(true_centers)[0]

    # Store first points belonging
    center_belonging.append(np.where(true_centers == one_point)[0][0])
    
    randomness = [random.gauss(0, 1) for i in range(d)] #array of gaussians
    data = np.array([one_point + randomness])

    # Create cluster 1
    while len(data) < N/2:
        ### Select first center
        one_point = true_centers[0]
        #print("one_point", one_point)

        randomness = [random.gauss(0, 1) for i in range(d)] #array

        one_point = one_point + randomness

        data = np.append(data, [one_point], axis=0)

    # Create cluster 2
    while len(data) < N:
        ### Select second center
        one_point = true_centers[1]

        # Store center belonging
        #center_belonging.append(np.where(true_centers == one_point)[0][0])

        randomness = [random.gauss(0, 1) for i in range(d)] #array

        one_point = one_point + randomness

        data = np.append(data, [one_point], axis=0)
    
    # Plot data (optional)
    if plot_yesno == True and d == 2:
        plt.scatter(data[:,0], data[:,1])
        plt.show()
    
    # Append true assignment
    #data = np.append(data, [[i] for i in center_belonging], axis=1)


    if save_data == True:
        np.savetxt("Data/" + filename + ".txt", data, delimiter=",")

    return data

#print(make_clusters(N=10))

#print("FINAL RESULT data: ", make_clusters_array(100, 2, 3))

# A function for generating custom random blobs/clusters
# The idea is to use this only in the beginning to create some desired
# datasets, store them, and then read from the files. This function
# is only intended to be used before the analysis part of the study takes
# place.

#make_clusters(N=500, d=5, K=7, save_data=True)