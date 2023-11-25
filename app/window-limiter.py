from flask import Flask, request, Response, jsonify

import time, requests

"""
    A dummy API that returns a "status OK" message for use with 
    various rate limiters under development.
"""

app = Flask(__name__)

api_address = "http://api:8080/"

# Configuration dictionary of requests/second allowed
rates = {
    "default" : 3
}
# Record of the requests made
incoming_requests = {}

# "forward a request" reference: https://stackoverflow.com/questions/6656363/proxying-to-another-web-service-with-flask
@app.route("/")
def rate_limit():
    # Determine if the request should be forwarded to the app or rate limited
    allowed = True

    # Identify the source of the incoming request
    identity = request.remote_addr
    rate = rates["default"]
    # By rounding down to the nearest whole second we automatically bin requests to within a second
    time_recv = int(time.time())

    # Record the request
    if identity not in incoming_requests:
        incoming_requests[identity] = {}
    
    if time_recv not in incoming_requests[identity]:
        incoming_requests[identity][time_recv] = 0

    incoming_requests[identity][time_recv] += 1

    # Check if the recorded request is within the limits
    if incoming_requests[identity][time_recv] > rate:
        allowed = False

    if allowed:
        # Allowed - Make API call
        resp = requests.get(api_address)
        response = Response(resp.content, resp.status_code)
    else:
        # Not allowed - return 429
        response = jsonify("Status: NOK")

    return response, 429
