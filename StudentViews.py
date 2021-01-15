from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json
from Authentication import token_required
conn = Database_connection().cnxn
cur = conn.cursor()


@app.route('/students')
def getStudents():
    query = 'Exec GET_STUDENTS;'

    cur.execute(query)
    r = [dict((cur.description[i][0], str(value))
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'status': 200, 'result': r})


@app.route('/students_courses/<studentId>')
def coursesOfStudent():
    studentId = requests.args['studentId']
    query = 'Exec GET_COURSES_BY_STUDENT ' + str(studentId)
    cur.execute(query)
    r = [dict((cur.description[i][0], str(value))
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'status': 200, 'result': r})
