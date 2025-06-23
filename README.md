# Anomaly Detection

###### Ariel University, Israel || Semester A - 2022

## Description

This project implements an anomaly detection system for network data analysis. The system uses machine learning algorithms to identify anomalous network connections from physical hosts. The data is provided in CSV format and includes network connection features such as duration, source bytes, and destination bytes.

## Features

- **DBSCAN Clustering**: Uses Density-Based Spatial Clustering of Applications with Noise (DBSCAN) algorithm for anomaly detection
- **Interactive UI**: Command-line interface for real-time anomaly prediction
- **Docker Support**: Containerized application for easy deployment and usage
- **Performance Metrics**: F1-score evaluation for model performance assessment
- **Network Data Analysis**: Specialized for network connection anomaly detection


## Dataset Information

The project uses two main datasets:
- **conn_attack.csv**: Contains network connection records with features:
  - `record_id`: Unique identifier for each connection
  - `Duration_`: Duration of the connection
  - `src_bytes`: Source bytes transferred
  - `dst_bytes`: Destination bytes transferred
- **conn_attack_anomaly_labels.csv**: Contains ground truth labels:
  - `id`: Record identifier (matches record_id from main dataset)
  - `label`: Anomaly label (0 for normal, -2 for anomaly)

## Installation

### Prerequisites
- Python 3.x
- pip package manager

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/VictoKu1/Anomaly_Detection.git
cd Anomaly_Detection
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies

The project requires the following Python packages:
- `matplotlib`: For data visualization
- `sklearn`: For machine learning algorithms (DBSCAN)
- `pandas`: For data manipulation and analysis
- `numpy`: For numerical computations

## Usage

### Running the UI Application

1. **Direct Python execution**:
```bash
python anomaly_detection_ui.py
```

2. **Interactive input**: The application will prompt you to enter:
   - Duration of the connection
   - Source bytes
   - Destination bytes

3. **Output**: The system will provide:
   - Prediction result (anomaly or normal)
   - F1-score of the model performance

### Docker Usage

1. **Install Docker requirements**:
```bash
pip install -r requirements.txt
```

2. **Build the Docker image**:
```bash
docker build -t anomaly_detection_ui .
```

3. **Run the Docker container**:
```bash
docker run -it anomaly_detection_ui
```

## Technical Details

### Algorithm
- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
  - `min_samples=150`: Minimum number of samples in a neighborhood
  - `n_jobs=-1`: Uses all available CPU cores for parallel processing

### Model Performance
- The system evaluates performance using F1-score
- Labels are mapped as follows:
  - `-2` → `-1` (anomaly)
  - Other values → `0` (normal)

### Data Processing
- Records are indexed by `record_id`
- Features are normalized and processed for clustering
- Anomaly detection is performed on the feature space

## Analysis and Documentation

- **Jupyter Notebook**: `Task1 - Anomaly Detection.ipynb` contains detailed analysis, visualizations, and model development
- **PDF Report**: `Task1 - Anomaly Detection.pdf` provides comprehensive documentation of the analysis process

## Output

The system generates:
- Real-time predictions for new network connections
- Model performance metrics (F1-score)
- `output.csv` file with detailed results



## License

This project is part of an academic course at Ariel University, Israel.

---
