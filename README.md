# Weather Query Service
Dockerized application that reads data in from `seattle-weather.csv` and can be queried at the `/query` endpoint

## Dependencies
* Docker

## Usage
* To launch the service and the test service, run `docker compose up`
* This will launch the Flask server on port 5001 and run the test image
  * Note: The test image may start before the server is ready to accept requests, in this case the test container will restart and attempt to connect again. The output of the test container can be verified to confirm it successfully queried the server
* To use the service, open the output url provided by `docker compose up` which will open to the home page showing the service is running
* With the service running, all of the headers in the source data can be investigated at `/query?<header>=<value>`
  * Examples:
    * `/query?date=2012-06-04`
    * `/query?weather=rain`
    * `/query?weather=rain&limit=5`
