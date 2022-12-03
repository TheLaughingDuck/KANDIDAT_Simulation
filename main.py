# Load Packages
import matplotlib.pyplot as plt

# Local packages
#import seeds
import random_data
import kmeans
import numpy as np


# Create or Load Data
points = random_data.make_clusters(100, d=2, K=20)

# Run Initialization
#seed = seeds.plusplus(points, K=10)


# Run k-means
#print("Printing seed")
#print(seed)

#kmeans=KMeans(n_clusters = 5, init=seed, n_init=1).fit(points)
#clusters=KMeans(n_clusters = 5, n_init=1).fit(points)
#points = np.array([[1,2], [1.2,2.3], [3,4], [3.2,4.2], [1,2.2]])
centers = kmeans.kmeans_func(points, seed_method="kaufman", K=20, nstarts=1)

print(centers)

# Run Evaluation


# Present Evaluation (and Plot)
# MOVED TO kmeans.py
if len(points[0]) == 2 and False:
    #Plot data
    plt.scatter(points[:,0], points[:,1], marker=".")
    
    #Plot seed
    #plt.scatter(seed[:,0], seed[:,1], color="red", marker=".")

    #Plot final centers
    plt.scatter(centers[:,0], centers[:,1], color="orange", marker="*")

    # Show plot
    plt.show()