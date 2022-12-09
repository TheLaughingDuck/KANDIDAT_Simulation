import numpy as np
import kmeans
import random_data


from statistics import mode

#arr[(arr==1)]


# Column 1: Data, column 2: true label.
arr=np.array([[1,1],[2,1],[3,2],[4,1],[5,1],[6,2],[7,1],[8,1],[9,1],[10,2],[11,2],[12,1],[13,1],[14,2],[15,2],[16,2],[17,2],[18,2], [19,1]])
#                1     1     1     1     2     2     2     1     2      1      1      1      1      2      2      2      2      2       1
kmeans_assignment = np.array([1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1])



'''
# Get true labels
true_labels = np.unique(arr[:,-1], axis=0) # Array of unique elements in true label column (last column)

# Array copy we can manipulate (also attaching kmeans assignment as column on the right)
data = np.append(arr, [[i] for i in kmeans_assignment], axis=1)


correctly_assigned = 0 # Count
for i in true_labels:
    print("Begin label: ", i)
    one_cluster = data[data[:,-2] == i] # Creates array of all points in true cluster i
    print("this_cluster:\n", one_cluster)

    # Find mode (in kmeans assignment)
    the_mode = mode(one_cluster[:,-1]) # Grab mode of last column
    print("the mode: ", the_mode)

    # Delete points belonging to the "assignment mode"
    data = np.delete(data, obj=data[:,-1] == the_mode, axis=0)
    print("Remaining data:\n", data)

    numb_popular_index = list(one_cluster[:,-1]).count(the_mode)

    print("Adding: ", numb_popular_index)
    correctly_assigned += numb_popular_index
    print("---------------------")

print("Correctly assigned: ", correctly_assigned/len(arr))'''

#from statistics import mode
def accuracy_func(arr, model_assignment):
    '''
    data: numpy array, with the last column containing *true* labels (coded by integers).

    model_assignment: numpy array, with the *assigned* labels (coded by integers) from the kmeans algorithm.

    Clearly it is assumed that model_assignment is based on the same ordering as in data.
    '''

    # Get true labels
    true_labels = np.unique(arr[:,-1], axis=0) # Array of unique elements in true label column (last column)

    # Array copy we can manipulate (also attaching kmeans assignment as column on the right)
    remaining_data = np.append(arr, [[i] for i in model_assignment], axis=1)

    correctly_assigned = 0 # Count
    for i in true_labels:
        #print("Begin label: ", i)
        one_cluster = remaining_data[remaining_data[:,-2] == i] # Creates array of all points in true cluster i
        #print("this_cluster:\n", one_cluster)

        # Find mode (in kmeans assignment)
        the_mode = mode(one_cluster[:,-1]) # Grab mode of last column
        #print("the mode: ", the_mode)

        # Delete points belonging to the "assignment mode"
        remaining_data = np.delete(remaining_data, obj=remaining_data[:,-1] == the_mode, axis=0)
        #print("Remaining data:\n", remaining_data)

        numb_popular_index = list(one_cluster[:,-1]).count(the_mode)

        #print("Adding: ", numb_popular_index)
        correctly_assigned += numb_popular_index
        #print("---------------------")

    #print("Correctly assigned: ", correctly_assigned/len(arr))
    
    return(round(correctly_assigned/len(arr), 2))



accuracy_func(arr, kmeans_assignment)