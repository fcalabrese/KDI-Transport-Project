# NOTE: FIRST INSTALL LIBRARY WITH pip install geopy
# run as python findAddress.py <path_to_source_csv> <path_to_output_csv>
# expects a column "latitude" and one "longitude"
import pandas as pd
from geopy.geocoders import Nominatim
import sys
from geopy.extra.rate_limiter import RateLimiter
from tqdm import tqdm

tqdm.pandas()

geolocator = Nominatim(user_agent="notMeAtAllISwearNoNoNo", timeout=10)
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)
df = pd.read_csv(sys.argv[1])  # read input csv
df["address"] = "Undefined"

for index, row in df.iterrows():
    df.loc[index, "address"] = str(row["latitude"]) + ", " + str(row["longitude"])

df["address"] = df["address"].progress_apply(reverse)
print("Process completed.")
df.to_csv(sys.argv[2])

