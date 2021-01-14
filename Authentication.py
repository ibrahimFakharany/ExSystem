from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json
import jwt 
import datetime
from functools import wraps
import sys
conn = Database_connection().cnxn
cur = conn.cursor()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        input_json = request.get_json(force=True)
        token =None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        print(token)
        if not token: 
            return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256']) 
            
        except: 
            print("Oops!", sys.exc_info()[1], "occurred.")
           
            return jsonify({'message' : 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated 


@app.route('/login_user')
def loginUser():
    input_json = request.get_json(force=True)
    loginType = input_json['type']
    username = input_json['username']
    password = input_json['password']

    query = 'EXEC loginUser '+'\''+username+'\''+','+'\''+password +'\''+','+ '\''+loginType+'\''
    cur.execute(query)
    row = cur.fetchone()
    r =  dict((cur.description[i][0], str(value)) for i, value in enumerate(row)) 
    token = jwt.encode({'userId' : r['Id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=15)}, app.config['SECRET_KEY'])
    
    return jsonify({'status': 200 ,'token': token})
    

