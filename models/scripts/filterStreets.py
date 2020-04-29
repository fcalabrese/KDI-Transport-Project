import pandas as pd
import csv

df = pd.read_csv("streets_long_lat.csv")

total = []
with open("streets_final.csv", "w") as csvfile:
    fieldnames = []
    csvfile.write(
        "start_latitude,start_longitude,finish_latitude,finish_longitude,type,oneway\n"
    )
    for ind, row in df.iterrows():
        print(str(ind / len(df)), end="\r")
        test = row["geometry"].split("(")[1]
        test = test.split(")")[0]
        test = test.split(", ")
        test = [x.split(" ") for x in test]
        csvfile.write(
            test[0][1]
            + ","
            + test[0][0]
            + ","
            + test[-1][1]
            + ","
            + test[-1][0]
            + ","
            + row["highway"]
            + ","
            + str(row["oneway"])
            + "\n"
        )

