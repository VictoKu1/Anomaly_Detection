# Docker container for running a github reposiory https://github.com/VictoKu1/Anomaly_Detection.git with anomaly detection python script, the docker container will run from itself an UI applicaion where the user can add an incident and get a prediction if the incident is an anomaly or not.

FROM python:3.7

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/VictoKu1/Anomaly_Detection.git

WORKDIR Anomaly_Detection
RUN pip install --upgrade pip
RUN pip install -r Anomaly_Detection/requirements.txt

# Copy UI application
COPY anomaly_detection_ui.py .

# Run the UI application
CMD ["python", "anomaly_detection_ui.py"]