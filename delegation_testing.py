'''
This file is dedicated to computations of the probability of good delegation
'''
import seeds
import random_data
import numpy as np
from ttictoc import tic, toc
import math
import random
import datetime

### One test
# N = 100
# K = 2

def delegation_test(N, d, K, l=100):
    '''
    This method takes the parameters and simulates 100 seedings of the plusplus method
    for the given dataset, and returns the estimated probability of good delegation.
    '''
    # Testing parameters
    num_datasets = 10
    num_seedings = 100
    tic()

    # Number of successes
    successes = 0

    data_trial = 1
    while data_trial <= num_datasets:
        data = random_data.make_clusters(N=N, d=d, K=K, length=l)
        unlabeled_data = np.delete(data, obj=-1, axis=1)

        seed_trial = 1
        while seed_trial <= num_seedings:
            #print("Doing trial ", trial)

            seed = seeds.plusplus(unlabeled_data, K=K)

            cluster_indexes = []
            for i in seed:
                index = unlabeled_data.tolist().index(i.tolist())
                cluster_indexes.append(data[:,-1][index])

            unique_clusters = len(set(cluster_indexes)) #len(np.unique(seeds.plusplus(data, K=K)[:,-1], axis=0))

            if unique_clusters == K:
                successes += 1

            seed_trial += 1
        data_trial += 1

    P = round(successes / (num_datasets * num_seedings), 3)
    now = datetime.datetime.now()
    print("-----------------------")
    print("Test parameters:\n", "N =", N, "\n d =", d, "\n K =", K, "\n l =", l)
    print("Time and Date: " + now.strftime("%Y-%m-%d %H:%M:%S"))
    print("RESULTS:")
    print("Simulated P of good delegation: ", P)
    print("Estimated P of good delegation: ", round(plusplus_estimation(K=K, d=d, length=l),3))
    #print("Estimated P of good delegation: ", round(math.factorial(K)/K**K, 4))
    print("Elapsed Time: ", round(toc(), 2), " seconds")



def simulate_distance(dimension, length):
    ### Function for simulating the average distance
    # between two points in a d-dimensional hypercube

    cumulative_distance = 0
    for i in range(1000):
        point_1 = [random.random()*length for i in range(dimension)]
        point_2 = [random.random()*length for i in range(dimension)]
        cumulative_distance += math.dist(point_1, point_2)

    return cumulative_distance / 1000



def plusplus_estimation(K, d, length):
    # Setup
    product = 1
    D2 = (simulate_distance(dimension=d, length=length))**2
    C2 = (math.sqrt(2) * math.gamma((K+1)/2)/math.gamma(K/2))**2
    b = 1
    while b <= K-1:
        product *= (D2 * (K-b)) / (b*C2 + (K-b)*D2)
        b += 1

    return product
    #starts = math.log(1-0.95)/math.log(1-product)
    #print("Results for K =", K, ", d =", d, ", l =", length)
    #print("Plusplus Estimated P of good delegation: ", round(product,5))
    #print("Suggested number of starts: ", math.ceil(starts))
    #print("------------------------------------")

#plusplus_estimation(K=5,d=2,length=10)





delegation_test(N=1000, d=20, K=4, l=500)