
#! /usr/bin/env python

import os
from datetime import datetime

from flask import Flask, request, redirect, url_for, jsonify
from markupsafe import escape
from flask_debugtoolbar import DebugToolbarExtension

FLASK_DEFAULT_PORT:int = 5000

app = Flask(__name__)

def get_response(username:str=None) -> dict:
    now_utc:datetime = datetime.utcnow()
    now_iso_ts:str = now_utc.isoformat(sep=' ', timespec='microseconds')
    return {
        "id": id(now_utc),
        "name": username if username else "Anonymous",
        "timestamp": now_iso_ts
    }

@app.route("/")
def index():
    """
    Default landing url "/" will be internally redirected to "/time"
    """
    internal_redirect_url:str = url_for('simple_timestamp')
    return redirect(internal_redirect_url)

@app.route("/time")
def simple_timestamp():
    """
    Simple implementation
    """
    return get_response()

@app.route("/time/<string:username>", methods = ['GET', 'POST', 'PUT'])
def hello_timestamp(username:str):
    """
    Full fledged method
    """
    if 'GET' == request.method:
        safe_username:str = escape(username)
        return get_response(username=safe_username)
    else:
        http_method = request.method
        err_msg_as_json = jsonify({"error": f"[Forbidden Access] Invalid method: {http_method}"})
        return err_msg_as_json, 403


def server_info(flask_server_app:Flask):
    #
    # Note either start flask usin --debug 
    # or 
    # set Environment Variable as: export FLASK_DEBUG=1
    #
    if flask_server_app.debug:
        print('Flask App supported URIs:')
        with flask_server_app.test_request_context():
            print(f"Index: {url_for('index')}")
            print(f"simple_timestamp: {url_for('simple_timestamp')}")
            # print(url_for('simple_timestamp', next='/'))
            print(f"hello_timestamp: {url_for('hello_timestamp', username='Productive.Analytics')}")

def server_debug(flask_server_app:Flask):
    flask_server_app.secret_key = 'DEBUG_KEY_4_FLASK'
    toolbar = DebugToolbarExtension(flask_server_app)

###
### DEBUG / INFO
###
server_info(flask_server_app=app)
# server_debug(flask_server_app=app)


if __name__ == '__main__':
    port:int = int(os.environ.get('PORT', FLASK_DEFAULT_PORT))
    debug_flag:bool = bool(os.environ.get('FLASK_DEBUG', False))

    ### CALL BEFORE RUN to show the Flask server info
    server_info(flask_server_app=app)

    app.run(host='0.0.0.0', port=port, debug=debug_flag)