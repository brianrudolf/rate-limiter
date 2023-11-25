import requests, time

"""
    A load generator designed to drive load to test 
    various rate limiter strategies.
"""

address = "http://limiter:8080/"

start = int(time.time())

# Naive initial approach to make fast calls
for i in range(10000):
    resp = requests.get(address)
    time_delta = int(time.time()) - start
    if time_delta % 10 == 0:
        print("Making call {}".format(i))
    time.sleep(0.2)
