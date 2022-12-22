# UI which is being called by the Dockerfile
# and allows the user to add an incident to get a prediction
# if the incident is an anomaly or not.

# The model which is being used is DBSCAN
# and the data are conn_attack.csv and conn_attack_anomaly_labels.csv
# which is a labeled dataset.

import pandas as pd
from sklearn.metrics import f1_score
from sklearn.cluster import DBSCAN
import sys

# Read the data
df = pd.read_csv("conn_attack.csv", names=["record_id", "Duration_", "src_bytes", "dst_bytes"], index_col="record_id")
target = pd.read_csv("conn_attack_anomaly_labels.csv", names=["id", "label"], index_col="id")  # 0 outlier 1 inline

# A mapping function to fit the correct labels

def _map(x):
    return -1 if x == -2 else 0

if __name__ == "__main__":
    try:
        Duration_, src_bytes_, dst_bytes_ = int(input("Duration_:                        ")), int(input("src_bytes:                        ")), int(input("dst_bytes:                        "))
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)

    dbs = DBSCAN(min_samples=150, n_jobs=-1)
    dbs_labels = pd.Series(dbs.fit_predict(df)).apply(lambda x: _map(x))

    # Predict the incident
    pred = dbs.fit_predict([[Duration_, src_bytes_, dst_bytes_]])

    # Print the prediction
    print("\nThe incident is:                 ", _map(pred[0]))

    # Calculate the f1_score using the true labels
    f1_score = f1_score(target["label"], dbs_labels)
    print("The F1 score of the model is:\t", f1_score)



























