from tabulate import tabulate
import numpy as np
import kmeans
import datetime

### LOAD DATA
# Simple synthetic dataset
simple_data = np.loadtxt("Data/simple_data.txt", delimiter=",")

# Complex (large) synthetic dataset
complex_data = np.loadtxt("Data/complex_data.txt", delimiter=",")

# All iris attributes are interesting. K=3
iris_data = np.loadtxt("Data/iris.txt", delimiter=",", usecols=(0,1,2,3,4))

# Seeds (the last column indicates type. There are 3 types/clusters)
seed_data = np.loadtxt("Data/seeds_dataset.txt", delimiter="\t", usecols=(0,1,2,3,4,5,6,7))

# 10 clusters?
wine_red_data = np.loadtxt("Data/winequality-red.csv", delimiter=";", skiprows=1)
wine_white_data = np.loadtxt("Data/winequality-white.csv", delimiter=";", skiprows=1)
wine_data = np.append(wine_red_data, wine_white_data, axis=0)


### CREATE DATA FORMAT
data = [["UnifRandom"],
        ["k-means++"],
        ["Kaufman"]]

#### RUN TESTS ON ALL DATASETS

## VV ---------- Unif RANDOM ---------- VV
# UnifRandom - SIMPLE
random_simple_test = kmeans.kmeans_func(simple_data, seed_method="random", K=5, nstarts=10, table_output=True)
data[0].extend([random_simple_test])

# UnifRandom - KOMPLEX
random_complex_test = kmeans.kmeans_func(complex_data, seed_method="random", K=20, nstarts=10, table_output=True)
data[0].extend([random_complex_test])

# UnifRandom - IRIS
random_iris_test = kmeans.kmeans_func(iris_data, seed_method="random", K=3, nstarts=10, table_output=True, true_labels_included=True)
data[0].extend([random_iris_test])

# UnifRandom - SEEDS
random_seed_test = kmeans.kmeans_func(seed_data, seed_method="random", K=3, nstarts=10, table_output=True, true_labels_included=True)
data[0].extend([random_seed_test])
## ^^ ---------- Unif RANDOM ---------- ^^



## VV ---------- PLUS PLUS ---------- VV
# PlusPlus - SIMPLE
plus_simple_test = kmeans.kmeans_func(simple_data, seed_method="plusplus", K=5, nstarts=10, table_output=True)
data[1].extend([plus_simple_test])

# PlusPlus - KOMPLEX
plus_complex_test = kmeans.kmeans_func(complex_data, seed_method="plusplus", K=20, nstarts=10, table_output=True)
data[1].extend([plus_complex_test])

# PlusPlus - IRIS
plus_iris_test = kmeans.kmeans_func(iris_data, seed_method="plusplus", K=3, nstarts=10, table_output=True, true_labels_included=True)
data[1].extend([plus_iris_test])

# PlusPlus - SEEDS
plus_seed_test = kmeans.kmeans_func(seed_data, seed_method="plusplus", K=3, nstarts=10, table_output=True, true_labels_included=True)
data[1].extend([plus_seed_test])
## ^^ ---------- PLUS PLUS ---------- ^^



## VV ---------- KAUFMAN ---------- VV
# Kaufman - SIMPLE
kaufman_simple_test = kmeans.kmeans_func(simple_data, seed_method="kaufman", K=5, nstarts=1, table_output=True)
data[2].extend([kaufman_simple_test])

# Kaufman - KOMPLEX
#kaufman_complex_test = kmeans.kmeans_func(complex_data, seed_method="kaufman", K=20, nstarts=1, table_output=True)
#data[2].extend([kaufman_complex_test])
data[2].extend([["test", "test", "test"]])

# Kaufman - IRIS
kaufman_iris_test = kmeans.kmeans_func(iris_data, seed_method="kaufman", K=3, nstarts=1, table_output=True, true_labels_included=True)
data[2].extend([kaufman_iris_test])

# Kaufman - SEEDS
kaufman_seed_test = kmeans.kmeans_func(seed_data, seed_method="kaufman", K=3, nstarts=1, table_output=True, true_labels_included=True)
data[2].extend([kaufman_seed_test])
## ^^ ---------- KAUFMAN ---------- ^^



### PRODUCE TABLE
# Possibly produce latex table
column_headers = ["Simple", "Complex", "Iris", "Seeds"]

TABLE = tabulate(data, headers=column_headers, tablefmt="grid")

print(TABLE)

print("The above table will also be written/saved in Data/Testing_output_tables.txt")

with open("Data/Testing_output_tables.txt", "a") as f:
    now = datetime.datetime.now()

    f.write("The following table was created on " + now.strftime("%Y-%m-%d %H:%M:%S"))
    f.write("\n\n")
    f.write(TABLE)
    f.write("\n\n\n")
    f.write(tabulate(data, headers=column_headers, tablefmt="latex"))
    f.write("\n\n\n\n")
    f.write("-----------------------------------------------")
    f.write("\n\n\n\n")


### COPY PASTA
## VV ----------Unif RANDOM---------- VV
## ^^ ----------Unif RANDOM---------- ^^