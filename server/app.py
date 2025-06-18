#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# This runs before every request
@app.before_request
def app_path():
    # Store the current working directory in Flask's global `g`
    g.path = os.path.abspath(os.getcwd())

# Main route
@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    status_code = 200
    headers = {}

    # Return a full HTTP response using make_response
    return make_response(response_body, status_code, headers)

# Placeholder test for CodeGrade
def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1

if __name__ == '__main__':
    app.run(port=5555, debug=True)
