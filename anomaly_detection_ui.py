# UI which is being called by the dockerfile and allows the user can add an incident and get a prediction if the incident is an anomaly or not, the model which is being used is DBSCAN and the data is the conn_attack.csv and conn_attack_anomaly_labels.csv which is a labeled dataset

import pandas as pd
from sklearn.metrics import  f1_score
from sklearn.cluster import DBSCAN


# Read the data
df = pd.read_csv("conn_attack.csv", names=["record_id", "Duration_", "src_bytes", "dst_bytes"], index_col="record_id")
target = pd.read_csv("conn_attack_anomaly_labels.csv", names=["id", "label"], index_col="id")# 0 outlier 1 inlier


# Ask for the incident data
duration_ = int(input("Enter the duration:"))
src_bytes_ = int(input("Enter the src_bytes:"))
dst_bytes_ = int(input("Enter the dst_bytes:"))

DBS = DBSCAN(min_samples=150, n_jobs=-1)
DBS_labels = pd.Series(DBS.fit_predict(df)).apply(lambda x: _map(x))

# A mapping fuction to fit the correct labels
def _map(x):
    if x == -1:
        return 0
    return 1

# Predict the incident
prediction = DBS.fit_predict([[duration_, src_bytes_, dst_bytes_]])

# Print the prediction
print("The incident is", _map(prediction[0]))

# Calculate the f1_score using the true labels
f1_score = f1_score(target["label"], DBS_labels)
print("The F1 score of the model is", f1_score)