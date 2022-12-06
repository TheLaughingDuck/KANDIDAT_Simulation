# Load Packages

# Local packages
import random_data
import kmeans
import numpy as np


### LOAD OR CREATE DATA
#points = np.loadtxt("Data/repeat_consumption/reddit_sample/train.csv", delimiter=",", usecols=(0,1))
data = random_data.make_clusters(1000, d=2, K=30)


### RUN K-MEANS
#points = np.array([[1,2], [1.2,2.3], [3,4], [3.2,4.2], [1,2.2]]) #Test
centers = kmeans.kmeans_func(data, seed_method="random", K=30, nstarts=10)[0]
#print(centers)



### RUN EVALUATION


### PRESENT EVALUATION
