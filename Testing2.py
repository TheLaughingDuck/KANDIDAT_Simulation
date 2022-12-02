
K=10
k=[0]

while len(k) < K:
    print("Beginning, k: ", k)
    k.append(0)


import pandas as pd

def plusplus(K):
    print("The Beginning")
    seed = pd.DataFrame([[1,2,3]], columns=["A"])

    while len(seed) < K:
        print("Beginning lap(seed length): ", len(seed))
        
        seed.concat()

        print("PRINTING SEED: ", seed)
        print("PRINTING SEED LENGTH: ", len(seed))

    #points.drop(columns=['D2'])

    return seed