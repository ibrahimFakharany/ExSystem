from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json


conn = Database_connection().cnxn
cur = conn.cursor()

@app.route('/create_topic')
def createQuestion():
    
    
