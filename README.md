# Telco Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to churn using a Decision Tree Classifier.

The project includes:

* Data understanding and preparation
* Data cleaning
* Feature engineering
* Exploratory data analysis
* Decision Tree model development
* Model evaluation
* Feature importance analysis
* Model saving
* REST API for churn prediction

## Dataset

The project uses the Telco Customer Churn dataset.

The target variable is:

* `Churn = Yes` – Customer is likely to churn
* `Churn = No` – Customer is likely to stay

The target was converted to:

* `1` = Churn
* `0` = No Churn

## Feature Engineering

Two additional features were created:

### TenureGroup

Customers were grouped based on their tenure:

* 0-1 Year
* 1-2 Years
* 2-4 Years
* 4+ Years

### AvgMonthlySpend

Calculated using:

```text
AvgMonthlySpend = TotalCharges / Tenure
```

This provides an estimate of the customer's average monthly spending.

## Model Development

Two Decision Tree configurations were tested.

| Model                   | Accuracy | Precision | Recall | F1 Score |
| ----------------------- | -------: | --------: | -----: | -------: |
| Decision Tree - Depth 4 |   0.7331 |    0.4983 | 0.7861 |   0.6100 |
| Decision Tree - Depth 8 |   0.7324 |    0.4974 | 0.7701 |   0.6044 |

The **Decision Tree with Depth 4** was selected as the final model because it performed slightly better across all four evaluation metrics and is simpler to interpret.

## Model Evaluation

The final model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

The final model achieved approximately:

* **Accuracy:** 73.31%
* **Precision:** 49.83%
* **Recall:** 78.61%
* **F1 Score:** 61.00%

Recall was given particular importance because identifying customers who are actually going to churn can help the telecom company take retention actions.

## Feature Importance

The most important features identified by the final Decision Tree include:

1. Contract - Two year
2. Contract - One year
3. Internet Service - Fiber optic
4. Tenure
5. Streaming Movies
6. Total Charges
7. Monthly Charges
8. Average Monthly Spend
9. Payment Method - Electronic check

Contract type and tenure were among the most influential features in the model.

## Project Structure

```text
customer_churn_project/
│
├── data/
│   └── telcoCustomerChurn.csv
│
├── notebook/
│   └── churn_analysis.ipynb
│
├── api/
│   └──  app.py
│
├── model/
│   └──  churn_model.pkl
│
├── requirements.txt
└── README.md
```

## Installation

Make sure Python 3 is installed.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Notebook

Open the notebook:

```text
notebook/churn_analysis.ipynb
```

Run the cells in order to perform the complete analysis and model development.

The trained model is saved as:

```text
churn_model.pkl
```

## Running the API

Go to the API directory:

```bash
cd api
```

Start the Flask application:

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoint

### POST `/predict`

Endpoint:

```text
http://127.0.0.1:5000/predict
```

The endpoint accepts customer information as JSON and returns the predicted churn status and churn probability.

### Sample Request

```json
{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 80.5,
    "TotalCharges": 402.5
}
```

### Sample Response

```json
{
    "prediction": "Yes",
    "churn_probability": 0.82
}
```

The probability shown above is an example. The actual probability depends on the customer information and trained model.

## Testing the API

The API can be tested using Postman, Thunder Client, or curl.

Example using curl:

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 80.5,
    "TotalCharges": 402.5
}'
```

## Error Handling

The API returns an error response when invalid or missing input is provided.

Example:

```json
{
    "error": "No JSON data provided"
}
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* Joblib
* Jupyter Notebook

## Conclusion

The Decision Tree model provides a simple and interpretable approach for predicting telecom customer churn. The model can help identify customers with a higher likelihood of churn so that targeted retention actions can be considered.
