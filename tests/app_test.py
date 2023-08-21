"""
Test script for weather service
"""
import os
import requests

running_in_docker = os.environ.get("RUNNING_IN_DOCKER", False)
print("RUNNING IN DOCKER", running_in_docker)

BASE_URL = (
    "http://weather-service:5001" if running_in_docker else "http://127.0.0.1:5001"
)
print("BASE_URL", BASE_URL)

queries = [
    {"date": "2012-01-01"},
    {"weather": "drizzle"},
    {"weather": "rain", "limit": "5"},
    {"date": "2012-01-01", "limit": "10"},
]

tests = 0
errors = 0

base_response = requests.get(BASE_URL, timeout=60)
tests += 1
if base_response.status_code == 200:
    print("Service is running.")
else:
    errors += 1
    print("Service is not running or an error occurred.")

for query in queries:
    print(f"Testing {query}")
    response = requests.get(f"{BASE_URL}/query", params=query, timeout=60)
    tests += 1

    if response.status_code != 200:
        errors += 1
        print(f"Error: {response.status_code} - {response.text}")

print(f"Tests run: {tests}, Errors: {errors}")
