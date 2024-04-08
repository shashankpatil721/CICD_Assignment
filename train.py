# Introduce errors to simulate both actions failing
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

# Introduce an error by providing a non-existent file path
try:
    df = pd.read_csv("data/non_existent_file.csv")
    X = df.drop(columns=['Disease']).to_numpy()
    y = df['Disease'].to_numpy()
    labels = np.sort(np.unique(y))
    y = np.array([np.where(labels == x) for x in y]).flatten()

    model = LogisticRegression().fit(X, y)

    with open("model.pkl", 'wb') as f:
        pickle.dump(model, f)
except Exception as e:
    print("An error occurred:", e)
