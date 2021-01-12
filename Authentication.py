from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json

conn = Database_connection().cnxn
cur = conn.cursor()

@app.route('/login_user')
def loginUser():
    input_json = request.get_json(force=True)
    loginType = input_json['type']
    username = input_json['username']
    password = input_json['password']


    query = 'EXEC loginUser '+'\''+username+'\''+','+'\''+password +'\''+','+ '\''+loginType+'\''
    
    cur.execute(query)
    r = [dict((cur.description[i][0], str(value))
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'status': 200 ,'result': r})
    

    