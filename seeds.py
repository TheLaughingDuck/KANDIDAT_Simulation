import random
import math
import numpy as np

def random_seed(df, K):

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
    return None