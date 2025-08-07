# Hangover-prediction-sample-ML-flaskAPI
Handover Prediction in 4G/5G Networks Using Machine Learning
This project applies machine learning techniques to predict potential handover failures in 4G/5G telecom core networks. It focuses on analyzing session hang and mobility issues between PCRF and PGW, leveraging real-world-like datasets and producing actionable insights.

🔍 Problem Statement

Handover failures can lead to dropped calls, poor user experience, and network inefficiencies. The goal is to build a predictive model that identifies cells prone to session hang or handover failure, enabling proactive mitigation.

📦 Features

Data cleaning and preprocessing for telecom datasets

Feature engineering on signal metrics and session parameters

Model training (Random Forest Classifier)

Evaluation with precision, recall, F1-score, confusion matrix

Deployment-ready structure (no Streamlit dependency)

Designed for integration with observability dashboards or cloud apps

📁 Project Structure

handover-prediction/
│
├── data/
│ └── sample_handover_data.csv # Example telecom KPI and session records
│
├── src/
│ ├── data_preprocessing.py # Cleans and prepares data
│ ├── model_train.py # Model training and evaluation
│ └── predict.py # Inference module
│
├── app.py # Simple CLI or Flask-based app
├── requirements.txt
└── README.md

📊 Sample Features

signal_strength

RSRP, RSRQ

active_sessions

failed_handover_attempts

cell_load

QCI, bearer_type

🧠 Model

We use a RandomForestClassifier from scikit-learn due to its robustness and ability to handle categorical + numerical data.

✅ Evaluation Notes

Works well with engineered features like handover failure rate (%).

Small datasets benefit from balanced class weighting.

Model struggles if session-level logs are too noisy or lack timestamps.

Can be scaled to RAN or edge node logs with minimal changes.

🌐 Potential Integrations

Azure ML / AWS SageMaker for scalable training

Grafana/Prometheus for observability

Kafka for ingesting real-time KPI streams

Dockerized API deployment

🚀 Run Locally

Clone the repo:
git clone https://github.com/jsyamala/handover-prediction.git

Set up environment:
pip install -r requirements.txt

Run training:
python src/model_train.py

Predict:
python src/predict.py

📈 Future Work

Add LSTM model for time-series prediction

Real-time inference using Kafka + FastAPI

Feature importance visualization

🙌 Acknowledgements

Thanks to open telecom datasets and the 3GPP standards community for shaping domain knowledge.
