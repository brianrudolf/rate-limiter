from flask import Flask, request, Response, jsonify
from redis import Redis
from logging.config import dictConfig

import time, requests, os
import threading

"""
    A dummy API that returns a "status OK" message for use with 
    various rate limiters under development.
"""

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

api_address = os.environ["API_ADDRESS"]
api_port = os.environ["API_PORT"]
cache_address = os.environ["CACHE_ADDRESS"]

redis_server = Redis.from_url(f"redis://{cache_address}:6379/", decode_responses=True)

api_address = f"http://{api_address}:{api_port}/"

# Configuration dictionary of requests/second allowed
rates = {
    "default" : 3
}

@app.route("/")
def rate_limit():
    # Determine if the request should be forwarded to the app or rate limited
    allowed = True

    # Identify the source of the incoming request
    identity = request.remote_addr
    rate = rates["default"]

    # Round time stamp to nearest millisecond
    time_recv = round(time.time(), 3)

    # Remove old data
    removed = redis_server.zremrangebyscore(identity, 0, time_recv - 5)

    # Check if the recorded request is within the limits
    # Sum count for the past second
    total_req = 0

    past_req = redis_server.zrange(identity, time_recv-1, time_recv, byscore=True, withscores=True)
    total_req = len(past_req)
    # app.logger.info("Total requests: {}".format(total_req))
    # app.logger.info("Requests: {}".format(past_req))

    if total_req >= rate:
        allowed = False

    if allowed:
        # Add a time stamp to the sorted set. Assume we don't have more than one request per millisecond
        res = redis_server.zadd(identity, { time_recv : time_recv })
        # Allowed - Make API call
        resp = requests.get(api_address)
        response, code = Response(resp.content, resp.status_code), resp.status_code
    else:
        # Not allowed - return 429
        response, code = jsonify("Status: NOK"), 429

    return response, code
