import requests
import json
import pandas as pd

trentinoStations = []
st = pd.read_csv("../Public transports/Train/stations.csv")

for index, row in st.iterrows():
    trentinoStations.append(row["localita"].split("|")[0])


url = "http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/{stazione}/{treno}"
file1 = open("./codici-treno.txt", "r")
codici = file1.readlines()

with open("./train_schedule.txt", "w") as myfile:
    for actual in codici:
        print(codici.index(actual) / len(codici))
        array = actual.split("|")
        values = array[1].split("-")
        with requests.Session() as s:
            result = json.loads(
                s.get(url.format(treno=values[0], stazione=values[1][:-1])).text
            )
            if result["fermate"] is not None:
                inTrentino = False
                for i in result["fermate"]:
                    if i["stazione"] in trentinoStations:
                        inTrentino = True

                if inTrentino:
                    index = 1
                    for i in result["fermate"]:
                        myfile.write(
                            str(values[0])
                            + ","
                            + str(index)
                            + ","
                            + str(i["stazione"])
                            + ","
                            + str(i["id"])
                            + ","
                            + str(i["programmata"])
                            + "\n"
                        )
                        index += 1
