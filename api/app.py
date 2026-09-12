from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model pipeline
model = joblib.load("../model/churn_model.pkl")


def create_features(data):
    """Create features required by the trained model."""

    data["TotalCharges"] = pd.to_numeric(
        data["TotalCharges"],
        errors="coerce"
    )

    data["TotalCharges"] = data["TotalCharges"].fillna(0)

    # Create TenureGroup
    data["TenureGroup"] = pd.cut(
        data["tenure"],
        bins=[-1, 12, 24, 48, float("inf")],
        labels=[
            "0-1 Year",
            "1-2 Years",
            "2-4 Years",
            "4+ Years"
        ]
    )

    # Create AvgMonthlySpend
    data["AvgMonthlySpend"] = (
        data["TotalCharges"] /
        data["tenure"].replace(0, 1)
    )

    return data


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON data provided"
            }), 400

        # Convert JSON to DataFrame
        input_data = pd.DataFrame([data])

        # Create engineered features
        input_data = create_features(input_data)

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Churn probability
        probability = model.predict_proba(input_data)[0][1]

        return jsonify({
            "prediction": "Yes" if prediction == 1 else "No",
            "churn_probability": round(float(probability), 4)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)