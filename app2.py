from flask import Flask, jsonify, render_template, redirect, url_for
from flask_pymongo import PyMongo
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# Create engine
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

# UPDATE
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

# Define the flask app
app = Flask(__name__)


#??
import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")


# Set the main route
@app.route('/')
def welcome():
    return 'LESKE PUZZLE COLLECTION'


