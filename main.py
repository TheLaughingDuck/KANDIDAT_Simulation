# Load Packages
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Local packages
import seeds
import random_data


# Create or Load Data
points = random_data.make_clusters(100, d=2, K=5)

# Run Initialization
seed = seeds.plusplus(points, K=5)


# Run k-means
#print("Printing seed")
#print(seed)

kmeans=KMeans(n_clusters = 5, init=seed, n_init=1).fit(points)
#clusters=KMeans(n_clusters = 5, n_init=1).fit(points)


centers = kmeans.cluster_centers_

print(centers)

# Run Evaluation


# Present Evaluation
if len(points[0]) == 2:
    #Plot data
    plt.scatter(points[:,0], points[:,1], marker=".")
    
    #Plot seed
    plt.scatter(seed[:,0], seed[:,1], color="red", marker=".")

    #Plot final centers
    plt.scatter(centers[:,0], centers[:,1], color="orange", marker="*")

    # Show plot
    plt.show()