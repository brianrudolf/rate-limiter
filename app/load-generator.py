import requests, time, os

"""
    A load generator designed to drive load to test 
    various rate limiter strategies.
"""

limiter_address = os.environ["LIMITER_ADDRESS"]
limiter_port = os.environ["LIMITER_PORT"]
request_rate = os.environ["REQUEST_RPS"]

address = f"http://{limiter_address}:{limiter_port}/"

# start = int(time.time())

rate_sleep = 1 / float(request_rate)

# Naive initial approach to make fast calls
while True:
    resp = requests.get(address)
    # time_delta = int(time.time()) - start
    # if time_delta % 10 == 0:
    #     print("Making call {}".format(i))
    time.sleep(rate_sleep)
