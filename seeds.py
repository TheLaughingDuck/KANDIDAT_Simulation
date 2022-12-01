import random
import pandas as pd

def random_seed(df, K):
    #len(df) gives the number of rows.
    seed_rows = random.sample([i for i in range(0, len(df))], K) #Produces a list of selected row indexes.
    seed = df.iloc[seed_rows] # Grab selected rows.
    
    return seed


def plusplus():
    return None


def kaufman():
    return None