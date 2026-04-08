import pyotp
import sqlite3
import hashlib
import uuid
from flask import Flask, request
app = Flask(__name__)

db_name = "test.db"

@app.route('/')
def index():
    return 'Welcome to the hands-on lab for an evolution of password systems!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')

    