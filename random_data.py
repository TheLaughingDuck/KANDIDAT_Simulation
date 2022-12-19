import random
import numpy as np
import matplotlib.pyplot as plt


# Large "blank dataframe" N rows, d+1 columns.
# The extra column is reserved for "true" cluster affiliation.
#pd.DataFrame([[0 for i in range(d)]+[1] for j in range(N)] , columns=[k for k in range(0,d+1)])



def make_clusters(N, d=2, K=4, plot_yesno = False, save_data = False, length=100):

    if save_data == True:
        print("-----------------------")
        print("You have opted to save the cluster data in a file.")
        print("Please input filename. No file extension (.txt is automatically added)")
        filename = input(">>")

    ### Generate TRUE centers
    true_centers = np.array([[random.random()*length for i in range(d)] for i in range(K)])

    ## Store center belonging
    center_belonging = []

    one_point = random.choices(true_centers)[0]

    # Store first points belonging
    center_belonging.append(np.where(true_centers == one_point)[0][0])
    
    randomness = [random.gauss(0, 1) for i in range(d)] #array of gaussians
    data = np.array([one_point + randomness])

    while len(data) < N:
        ### Select one center, add some randomness and "store" the point
        one_point = random.choices(true_centers)[0]

        # Store center belonging
        center_belonging.append(np.where(true_centers == one_point)[0][0])

        randomness = [random.gauss(0, 1) for i in range(d)] #array
        one_point = one_point + randomness

        data = np.append(data, [one_point], axis=0)
    
    # Plot data (optional)
    if plot_yesno == True and d == 2:
        plt.scatter(data[:,0], data[:,1])
        plt.show()
    
    # Append true assignment
    data = np.append(data, [[i] for i in center_belonging], axis=1)


    if save_data == True:
        np.savetxt("Data/" + filename + ".txt", data, delimiter=",")

    return data

#print(make_clusters(N=10, d=2, K=4, plot_yesno=True))

#print("FINAL RESULT data: ", make_clusters_array(100, 2, 3))

# A function for generating custom random blobs/clusters
# The idea is to use this only in the beginning to create some desired
# datasets, store them, and then read from the files. This function
# is only intended to be used before the analysis part of the study takes
# place.

#make_clusters(N=500, d=5, K=7, save_data=True)