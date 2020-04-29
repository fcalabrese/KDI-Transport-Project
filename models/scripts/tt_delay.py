# get all stops
# for each stop, ask for all autobus that came the previous day
# for each data, extract just the bus id and the delay

import requests
import json
import sys

url = "https://app-tpl.tndigit.it/gtlservice/trips?&stopId={stopId}&type=U&limit=10000&refDateTime=2019-{month}-{day}T00:10:00.151Z"

buses = []
with open(
    "../Public transports/Urban Trento/delay/{day}.{month}.19.csv".format(
        day=sys.argv[1], month=sys.argv[2]
    ),
    "w",
) as myfile:
    myfile.write("tripId,delay\n")
    with requests.Session() as s:
        r = json.loads(s.get("https://app-tpl.tndigit.it/gtlservice/stops").text)
        for index, i in enumerate(r):
            print(index / 3711)
            string = s.get(
                url.format(stopId=i["stopId"], day=sys.argv[1], month=sys.argv[2])
            ).text
            if string != "":
                r = json.loads(string)
                for bus in r:
                    if bus["tripId"] not in buses:
                        buses.append(bus["tripId"])
                        if bus["delay"] is not None:
                            myfile.write(
                                str(bus["tripId"]) + "," + str(bus["delay"]) + "\n"
                            )
