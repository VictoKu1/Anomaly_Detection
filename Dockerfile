# Docker container for running a github reposiory
# https://github.com/VictoKu1/Anomaly_Detection.git
# with anomaly detection python script,
# the docker container will run from itself an UI applicaion
# where the user can add an incident and get a prediction if the incident is an anomaly or not.

FROM python:3

# Install dependencies
RUN pip install numpy pandas scikit-learn

# Copy the necessary files from the host machine to the container
COPY anomaly_detection_ui.py .
COPY conn_attack_anomaly_labels.csv .
COPY conn_attack.csv .

# Set the command to run when the container starts
CMD ["python", "anomaly_detection_ui.py"]






