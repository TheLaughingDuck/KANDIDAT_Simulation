import random
import pandas as pd
import math


def make_clusters(N, d, K):
    #Create empty dataframe
    data_points = pd.DataFrame([], columns=[i for i in range(0,d)])

    for i in range(0,K):
        true_center = [random.uniform(0,100) for i in range(0,d)] #Random true center.
        for j in range(0, N):
            one_point = [random.gauss(true_center[i], 1) for i in range(0,d)] #Generate the random point around the center.
            
            #Make it a dataframe
            one_point = pd.DataFrame([one_point], columns=[i for i in range(0,d)])

            #print("---------------")

            #print("Dataframe of points. ", f"i = {i}, ", f"j = {j}.")
            #print(points)

            #print("Dataframe of one point. ", f"i = {i}, ", f"j = {j}.")
            #print(one_point)

            #Add point to dataframe of points
            data_points = pd.concat([data_points, one_point], keys=list(data_points.columns), ignore_index=True)
    
    # Return the finished data.
    return data_points





def plusplus(df, K): #Dataframe, K clusters
    #Select first center (uniformly) random.
    seed_rows = random.sample([i for i in range(0, len(df))], 1)
    seed = df.iloc[seed_rows]
    df = df.drop(seed_rows)


    while len(seed) < K:
        print("Beginning lap(seed length): ", len(seed))
        ## Calculate all D(x_i) (each points distance to its closest center). Then square them.
        
        # Copy of df, with additional column "D2(x)" (containing None)
        #points = pd.DataFrame(df, columns=list(df.columns)+["D2"])
        points = df.assign(D2 = [None for i in range(len(df))])
        #print("len of points is", len(points))

        print("Another go!, seed length: ", len(seed))

        for i in range(len(points)):
            for j in range(len(seed)):
                #print("----------------------------")
                #print("Now going through i: ", i, " and j: ", j)
                #Calculate D()^2
                #print("PRINTING (before Euclidean)  list(points[\"D2\"])[i]: ", list(points["D2"])[i])
                D2 = dist.euclidean(list(df.iloc[i]), list(seed.iloc[j]))**2 #Squared Euclidean distance
                #print("Calculate D2 = ", D2)
                #print("PRINTING (after Euclidean)  list(points[\"D2\"])[i]: ", list(points["D2"])[i])

                if list(points["D2"])[i] == None or math.isnan(list(points["D2"])[i]):
                    new_column = list(points["D2"])
                    new_column[i] = D2
                    points["D2"] = new_column
                    #print(new_column)

                elif D2 < list(points["D2"])[i]:
                    new_column = list(points["D2"])
                    new_column[i] = D2
                    points["D2"] = new_column
                
                #print("PRINTING D2-column: ", list(points["D2"]))
                #print("PRINTING (last line)  list(points[\"D2\"])[i]: ", list(points["D2"])[i])


        ## Calculate the scaling constant
        #print("PRINTING points")
        #print(points)

        #(Might not need to calculate scale constant)
        #print("PRINTING scale_constant")
        scale_constant = 1/sum(points["D2"])
        #print(scale_constant)


        ## Implement a weighted sampler.
        #print("PRINTING df: ", df)
        #print("PRINTING D2-column: ", list(points["D2"]))
        #print("D2-column length: ", len(list(points["D2"])))
        #seed_row = random.choices(df, weights = list(points["D2"]), k=1)[0]
        seed_row = random.choices([i for i in range(len(points))], weights = list(points["D2"]), k=1)[0]

        print("PREPARING TO APPEND seed_row: ", seed_row)

        #append to seed
        seed = pd.concat([seed, df.iloc[seed_row]], keys=list(seed.columns), ignore_index=True)
        
        #drop seed_row from df
        df = df.drop(seed_row)

        print("PRINTING SEED: ", seed)
        print("PRINTING SEED LENGTH: ", len(seed))

    #points.drop(columns=['D2'])

    return seed