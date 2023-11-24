from flask import Flask, request, Response

import time, requests

"""
    A dummy API that returns a "status OK" message for use with 
    various rate limiters under development.
"""

app = Flask(__name__)

address = "http://localhost:5000/"

# "forward a request" reference: https://stackoverflow.com/questions/6656363/proxying-to-another-web-service-with-flask
@app.route("/")
def rate_limit():
    # Determine if the request should be forwarded to the app or rate limited
    resp = requests.get(address)


    response = Response(resp.content, resp.status_code)
    return response
