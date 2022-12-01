import matplotlib.pyplot as plt
import pandas as pd


import random



def plot_graph(data, points):
    pass


df1 = pd.DataFrame(
    {
        "X":[1,1.3,0.9, 3, 3.5, 3.3],
        "Y":[2,2.2,2.1, 4.1, 4.2, 4]
    }
)


# Set parameters
N = 10
d = 2 #Dimensions or Features
K = 2


# Create or Load Data
#Create empty dataframe
#points = pd.DataFrame([], columns=[i for i in range(0,d)])

# Large "blank dataframe" N rows, d+1 columns.
dframe = pd.DataFrame([[0 for i in range(d)]+[1] for j in range(N)] , columns=[k for k in range(0,d+1)]) 

print(dframe)

#plt.scatter(df1["X"], df1["Y"])
#plt.show()'




#pd.concat([b, c], keys=["x", "y"])

#pd.DataFrame({"1":[1,2,3,6,7,8], "2":[4,5,6,2,7,1], "3":[7,8,9,9,1,22], "4":[0,1,3,4,1,77], "5":[8,2,5,9,8,3]}) 

