import pandas as pd
import random



# Large "blank dataframe" N rows, d+1 columns.
# The extra column is reserved for "true" cluster affiliation.
#pd.DataFrame([[0 for i in range(d)]+[1] for j in range(N)] , columns=[k for k in range(0,d+1)])




# A function for generating custom random blobs/clusters
# The idea is to use this only in the beginning to create some desired
# datasets, store them, and then read from the files. This function
# is only intended to be used before the analysis part of the study takes
# place.
def make_clusters(N, d, K):
    #Create empty dataframe
    data_points = pd.DataFrame([], columns=[i for i in range(0,d)])

    for i in range(0,K):
        true_center = [random.uniform(0,100) for i in range(0,d)] #Random true center.
        for j in range(0, N):
            one_point = [random.gauss(true_center[i], 1) for i in range(0,d)] #Generate the random point around the center.
            
            #Make it a dataframe
            one_point = pd.DataFrame([one_point], columns=[i for i in range(0,d)])

            #print("---------------")

            #print("Dataframe of points. ", f"i = {i}, ", f"j = {j}.")
            #print(points)

            #print("Dataframe of one point. ", f"i = {i}, ", f"j = {j}.")
            #print(one_point)

            #Add point to dataframe of points
            data_points = pd.concat([data_points, one_point], keys=list(data_points.columns), ignore_index=True)
    
    # Return the finished data.
    return data_points