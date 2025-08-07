from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(name)
model = joblib.load('model/model.pkl')

@app.route('/')
def home():
return 'Handover Prediction Model is Running'

@app.route('/predict', methods=['POST'])
def predict():
data = request.get_json()
features = np.array(data['features']).reshape(1, -1)
prediction = model.predict(features)
return jsonify({'prediction': prediction.tolist()})

if name == 'main':
    app.run(debug=True)