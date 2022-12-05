# UI which is being called by the dockerfile and allows the user can add an incident and get a prediction if the incident is an anomaly or not, the model which is being used is DBSCAN and the data is the conn_attack.csv and conn_attack_anomaly_labels.csv which is a labeled dataset

import pandas as pd
from sklearn.metrics import f1_score
from sklearn.cluster import DBSCAN

# Read the data
df = pd.read_csv("conn_attack.csv",
                 names=["record_id", "Duration_", "src_bytes", "dst_bytes"],
                 index_col="record_id")
target = pd.read_csv("conn_attack_anomaly_labels.csv",
                     names=["id", "label"],
                     index_col="id")  # 0 outlier 1 inline

# Ask for the incident data
Duration_ = int(input("Enter the Duration_:\t"))
src_bytes_ = int(input("Enter the src_bytes:\t"))
dst_bytes_ = int(input("Enter the dst_bytes:\t"))


# A mapping function to fit the correct labels
def _map(x):
    return -1 if x == -2 else 0


dbs = DBSCAN(min_samples=150, n_jobs=-1)
dbs_labels = pd.Series(dbs.fit_predict(df)).apply(lambda x: _map(x))

# Predict the incident
pred = dbs.fit_predict([[Duration_, src_bytes_, dst_bytes_]])

# Print the prediction
print("\nThe incident is:\t\t\t", _map(pred[0]))

# Calculate the f1_score using the true labels
f1_score = f1_score(target["label"], dbs_labels)
print("\nThe F1 score of the model is:\t", f1_score)
