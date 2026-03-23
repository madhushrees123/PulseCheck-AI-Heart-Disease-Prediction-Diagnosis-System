from flask import Flask, request, jsonify
import pickle
import sqlite3
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Connect to SQLite database
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    sex INTEGER,
    result TEXT
)
''')
conn.commit()


# Home route
@app.route('/')
def home():
    return "CardioSense AI Backend Running!"


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Convert input to array
        features = np.array(data['features']).reshape(1, -1)

        # Apply scaling
        features = scaler.transform(features)

        # Predict
        prediction = model.predict(features)[0]

        result = "High Risk" if prediction == 1 else "Low Risk"

        # Save to database
        cursor.execute(
            "INSERT INTO predictions (age, sex, result) VALUES (?, ?, ?)",
            (data['features'][0], data['features'][1], result)
        )
        conn.commit()

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})


#Get history route
@app.route('/history', methods=['GET'])
def history():
    cursor.execute("SELECT * FROM predictions")
    rows = cursor.fetchall()
    return jsonify(rows)


# Run server
if __name__ == '__main__':
    app.run(debug=True)
