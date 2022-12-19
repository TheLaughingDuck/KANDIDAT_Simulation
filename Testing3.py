import random_data
import kmeans

data = random_data.make_clusters(N=1000, d=2, K=5)

object = kmeans.kmeans_func(data, seed_method="random", nstarts=1000, table_output=True, plot_yesno=True, K=5, true_labels_included=True)

#object2 = kmeans.kmeans_func(data, seed_method="plusplus", nstarts=10, table_output=True, plot_yesno=True, K=60, true_labels_included=True)

print(object)

#print(object2)