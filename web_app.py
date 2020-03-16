#! /usr/bin/env python

from flask import Flask

app = Flask(__name__)

req_counter = 0

@app.route('/')
def count() -> str:
    global req_counter
    req_counter += 1
    return 'Your are visitor # '+ str(req_counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0')