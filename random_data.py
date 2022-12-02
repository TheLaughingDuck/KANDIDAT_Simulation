import random
import numpy as np



# Large "blank dataframe" N rows, d+1 columns.
# The extra column is reserved for "true" cluster affiliation.
#pd.DataFrame([[0 for i in range(d)]+[1] for j in range(N)] , columns=[k for k in range(0,d+1)])



def make_clusters(N, d=2, K=4):
    
    # Create a numpy array

    # Generate TRUE centers
    true_centers = np.array([[random.randint(0,1000) for i in range(d)] for i in range(K)])

    one_point = random.choices(true_centers)[0]
    randomness = [random.gauss(0, 20) for i in range(d)] #array of gaussians
    data = np.array([one_point + randomness])

    #print("PRINTING FIRST data: ", data)

    while len(data) < N:
        #print("-----------------")
        #print("New While Loop Lap: ", len(data))

        one_point = random.choices(true_centers)[0]
        randomness = [random.gauss(0, 20) for i in range(d)] #array
        one_point = one_point + randomness

        #print("PRINTING data: ", data)
        #print("PRINTING one_point: ", one_point)
        data = np.append(data, [one_point], axis=0)

    
    return data

#print("FINAL RESULT data: ", make_clusters_array(100, 2, 3))

# A function for generating custom random blobs/clusters
# The idea is to use this only in the beginning to create some desired
# datasets, store them, and then read from the files. This function
# is only intended to be used before the analysis part of the study takes
# place.
