#!/usr/bin/env python

import flask

# Creation of little application
app = flask.Flask(__name__)

@app.route('/')
def index():
  return flask.render_template('index.html')     

# This line fires up the server if we want to run that file as a standalone application
if __name__ == '__main__':
    app.run(debug=True)  
# To put a different port    
#     app.run(debug=True, port=8888)  
