import pandas as pd
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

# concatenate all delay CSV
path = "../Public transports/Urban Trento/delay"
all_files = glob.glob(path + "/*.csv")
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)
df = df.replace(to_replace="None", value=np.nan).dropna()

# one-hot encoding
one_hot = pd.get_dummies(df["tripId"])
df = df.drop(df.columns[1], axis="columns")
df = df.join(one_hot)
df["delay"] = df.delay.astype(float)

# Split datasets
X = df.drop("delay", axis="columns")
y = df["delay"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create and fit model
regressor = SVR(kernel="rbf", verbose=True)
regressor.fit(X_train, y_train)
print(regressor.score(X_test, y_test))
