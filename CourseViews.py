from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json

conn = Database_connection().cnxn
cur = conn.cursor()

@app.route('/get_courses')
def getCourses():
    query = 'Exec get_courses '
    
    cur.execute(query)
    r = [dict((cur.description[i][0], str(value))
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'status': 200 ,'result': r})

@app.route('/add_course', methods=['POST'])
def addCourse():
    input_json = request.get_json(force=True)
    topic_id = input_json['Topic_id']
    course_name = input_json['course_name']


    query = 'EXEC create_course '+str(topic_id)+', '+'\''+ course_name+'\'' 
    cur.execute(query)
    conn.commit()
    return jsonify({'status': 200, "message":"added"})

@app.route('/update_course', methods=['POST'])
def updateCourse():

    if request.is_json:
        input_json = request.get_json(force=True)
        
        query = ""

        if 'crs_id' in input_json:
            crsId = input_json['crs_id']
            query +=str(crsId)+ ','
        else: 
            return jsonify({'status':500, 'message': 'course id is required'})
    
        if 'topic_id' in input_json:
            topicId = input_json['topic_id']
            query += str(topicId)+','
        if 'crs_name' in input_json:
            crsName = input_json['crs_name']
            query += '\''+crsName+'\''
        print('*********************'+query)
        query = 'EXEC update_course '+query
        cur.execute(query)
        conn.commit()
        return jsonify({'status':200, 'message': 'updated'})

    else :
        return jsonify({'status':500, 'message': 'undefined json request'})
    
@app.route('/delete_course/<int:courseId>', methods=['delete'])
def removeCourse(courseId):
    query = 'EXEC delete_course ' +str(courseId)
    cur.execute(query)
    conn.commit()
    return jsonify({"message":"removed"})

