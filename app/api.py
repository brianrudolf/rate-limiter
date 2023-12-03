from flask import Flask
import time

"""
    A dummy API that returns a "status OK" message for use with 
    various rate limiters under development.
"""

app = Flask(__name__)

@app.route("/")
def status():
    app.logger.info("Status: 200")
    return "Status: OK\n"
