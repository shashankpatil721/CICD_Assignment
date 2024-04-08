# Introduce an error to simulate training failure
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

# Introduce an error by attempting to fit a model without splitting the data
try:
    df = pd.read_csv("data/train.csv")
    X = df.drop(columns=['Disease']).to_numpy()
    y = df['Disease'].to_numpy()
    labels = np.sort(np.unique(y))
    y = np.array([np.where(labels == x) for x in y]).flatten()

    # Introduce an error by attempting to fit the model without splitting the data
    model = LogisticRegression().fit(X, y)

    with open("model.pkl", 'wb') as f:
        pickle.dump(model, f)
except Exception as e:
    print("An error occurred:", e)
