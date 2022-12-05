import random
import math
import numpy as np

def random_seed(df, K):
    raise Exception("random_seed must be rewritten for NumPy!")

    seed_rows = random.sample([i for i in range(0, len(df))], K) #Produces a list of selected row indexes.
    seed = df.iloc[seed_rows] # Grab selected rows.
    
    return seed


def plusplus(data, K):
    ### Select first center uniformly random
    index = random.randint(0, len(data)-1)
    seed = np.array([data[index]])
    data = np.delete(data, obj=index, axis=0)

    #print("data: ", data)

    while len(seed) < K:
        #print("----------------------")
        #print("Beginning lap. len(seed) = ", len(seed))

        ### Calculate all D2
        D2list = [None for i in range(len(data))]

        for i in range(len(data)):
            for j in range(len(seed)):
                # Calculate D2
                D2 = math.dist(data[i], seed[j])**2

                # Update D2
                #if math.isnan(D2list[i]):
                #    print("ALERT!!!!")
                #    print("NaN PROBLEM!!!!")
                #print("D2list: ", D2list)
                #print("i: ", i)
                if D2list[i] == None:
                    D2list[i] = D2
                else: D2list[i] = min(D2list[i], D2)

        #print("FINISHED D2-calculations")
        #print("D2list: ", D2list)

        ### Implement weighted sampler
        # Choose index, 
        index = random.choices([i for i in range(len(data))], weights=D2list)[0]
        #print("seed: ", seed)
        #print("data[index]: ", data[index])

        seed = np.append(seed, [data[index]], axis=0)
        data = np.delete(data, obj=index, axis=0)
        
        #print("RESULT OF ONE WHILE LAP:")
        #print("index: ", index)
        #print("seed: ", seed)
        #print("data: ", data)

        #print("----------------------")

    return seed

#print(plusplus_array(np.array([[1,2], [1.2,2.3], [3,4], [3.2,4.2], [1,2.2]]), K=2))




def kaufman(data, K):
    ### Calculate and select most central instance
    ## Calculate global average
    global_average = sum(data) / len(data) #I love numpy

    ## Select most central instance
    minimal_distance = None
    index = 0
    for i in range(len(data)):
        distance = math.dist(data[i], global_average)

        if minimal_distance is None:
            minimal_distance = distance
            index = i
        elif distance < minimal_distance:
            minimal_distance = distance
            index = i
    
    ## Relocate central point
    seed = np.array([data[index]])
    data = np.delete(data, obj=index, axis=0)
    
    # I fully trust everything up till this point.

    ### Do some form of cycle until seed is appropriate length
    while len(seed) < K:
        ## Calculate all different SUM C_{ji}
        C_sum = 0
        sum_list = []

        for i in range(len(data)):
            for j in range(len(data)):
                ## Calculate point j's closest distance to a center; D_j
                minimal_distance = None
                for c in range(len(seed)):
                    D_j = math.dist(data[j], seed[c])
                    if minimal_distance is None or D_j < minimal_distance:
                        minimal_distance = D_j
                ## Calculate the sum of C_ji for the current i.
                C_ji = 0
                if i != j:
                    C_ji = max(minimal_distance-math.dist(data[i], data[j]), 0)

                C_sum += C_ji
            
            sum_list.append(C_sum)
            C_sum = 0

        ## Select the maximizing points index
        best_index = sum_list.index(max(sum_list))

        ## Relocate new center
        seed = np.append(seed, [data[best_index]], axis=0)
        data = np.delete(data, obj=best_index, axis=0)

    print("PRINTING Kaufman SEED: ", seed)    
    return seed

#print(kaufman(np.array([[1,2], [1.2,2.3], [3,4], [3.2,4.2], [1,2.2]]), K=2))




def format_function():
    ### Three # indicates the beginning of a major important step in a function

    ## Two # indicates a substep under one major step. They are often superfluos.

    # One # is used for comments and small notes. For example:
    # Don't forget to add <functionality>
    
    pass