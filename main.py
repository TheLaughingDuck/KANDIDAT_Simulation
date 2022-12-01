# Load Packages
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.cluster import KMeans

# Local packages
import seeds
import random_data


# Create or Load Data
points = random_data.make_clusters(100, 2, 5)


# Run Initialization
seed = seeds.random_seed(points, 5)


# Run k-means
#a=KMeans(n_clusters = 2, )

# Run Evaluation


# Present Evaluation
if len(points.columns) == 2:
    plt.scatter(points[0], points[1])
    plt.scatter(seed[0], seed[1], color="orange", marker="*")
    plt.show()