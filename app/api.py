from flask import Flask
import time

"""
    A dummy API that returns a "status OK" message for use with 
    various rate limiters under development.
"""

app = Flask(__name__)

@app.route("/")
def status():
    # print("Received request at {}".format(time.time()))
    return "Status: OK\n"
