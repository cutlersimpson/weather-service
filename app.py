"""
Flask web service reading CSV file and outputting JSON with the ability to query the data
"""
from flask import Flask, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("seattle-weather.csv")


@app.route("/")
def home():
    """
    Default endpoint to confirm weather service is running
    """
    return "The weather query service is running"


@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to explicitly test 200 response from server
    """
    return "OK", 200


@app.route("/query", methods=["GET"])
def query_data():
    """
    Function to query weather data by dynamically searching CSV headers
    Returns: Results of query
    """
    query_params = request.args
    filtered_data = data.copy()

    headers = [col.lower() for col in data.columns]

    for param, value in query_params.items():
        param = param.lower()

        if param == "limit":
            continue

        if param not in headers:
            return {"error": f"Invalid query parameter: '{param}'"}, 400

        filtered_data = filtered_data[filtered_data[param] == value]

    if "limit" in query_params:
        limit = int(query_params["limit"])
        filtered_data = filtered_data.head(limit)

    return filtered_data.to_json(orient="records")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
