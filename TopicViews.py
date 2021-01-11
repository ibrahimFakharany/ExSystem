from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json


conn = Database_connection().cnxn
cur = conn.cursor()


@app.route('/get_topics')
def getTopics():
    query = 'EXEC get_topics'
    cur.execute(query)
    r = [dict((cur.description[i][0], str(value))
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'status': 200 ,'result': r})