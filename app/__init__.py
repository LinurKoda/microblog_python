#This is a init model

from flask import Flask #import from a flask package the class called Flask.

app = Flask(__name__) #__name__ : name variable of Python

from app import routes 
