from flask import Flask, request, render_template
import pickle
import pandas as pd

# ✅ import your existing class (DON’T rewrite it)
from src.feature_engineering import FeatureEngineering

application = Flask(__name__)

# -------------------------------
# Load saved artifacts
# -------------------------------
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
columns = pickle.load(open("models/columns.pkl", "rb"))
le = pickle.load(open("models/label_encoder.pkl", "rb"))

# -------------------------------
# Home route
# -------------------------------
@application.route('/')
def home():
    return render_template("index.html")

# -------------------------------
# Prediction route
# -------------------------------
@application.route('/predict', methods=['POST'])
def predict():

    try:
        # -------------------------------
        # Get form data
        # -------------------------------
        data = request.form.to_dict()
        df = pd.DataFrame([data])

        # -------------------------------
        # Convert numeric values
        # -------------------------------
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                pass

        # -------------------------------
        # ✅ Feature Engineering (IMPORTANT)
        # -------------------------------
        fe = FeatureEngineering(df)
        df = fe.apply()

        # -------------------------------
        # ✅ Encoding
        # -------------------------------
        df = pd.get_dummies(df)
        df = df.reindex(columns=columns, fill_value=0)

        # -------------------------------
        # ✅ Scaling
        # -------------------------------
        df = scaler.transform(df)

        # -------------------------------
        # ✅ Prediction
        # -------------------------------
        pred = model.predict(df)
        result = le.inverse_transform(pred)[0]

        return render_template("index.html", prediction_text=f"Result: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


# -------------------------------
# Run application
# -------------------------------
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)