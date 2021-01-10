from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json

conn = Database_connection().cnxn
cur = conn.cursor()

@app.route('/getTableIdentity/<string:tableName>')
def getTableIdentity(tableName):
    query = 'EXEC GET_TABLE_IDENTITY '+tableName
    cur.execute(query)
    r = cur.fetchall()
    return jsonify({'status': 200 ,'result': int(r[0][0])})