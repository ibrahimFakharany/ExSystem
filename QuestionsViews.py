from database import Database_connection
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, jsonify
from app import app
import json

conn = Database_connection().cnxn
cur = conn.cursor()

@app.route('/add_question', methods=['POST'])
def addQuestion():
    input_json = request.get_json(force=True)
    courseId= input_json['course_id']
    question= input_json['question']
    questionType = input_json['question_type']
    answer = input_json['answer']
    
    query = 'EXEC add_question '+ str(courseId) + ',' + '\'' + question + '\'' + ',' + '\'' + questionType + '\'' + ',' +'\''+ answer+'\''
    
    if questionType == 'MCQ':
        ans_A = input_json['ans_a']
        ans_B = input_json['ans_b']
        ans_C = input_json['ans_c']
        ans_D = input_json['ans_d']
        print('the question is MCQ')
        query +=','+ '\'' + ans_A + '\'' + ',' + '\'' + ans_B + '\'' + ',' + '\'' + ans_C + '\'' + ',' + '\'' + ans_D + '\''

    r = cur.execute(query)
    conn.commit()
    return jsonify({'status': 200, "message":"added"})


@app.route('/generate_exam', methods=['POST'])
def generateExam():
    input_json = request.get_json(force=True)
    courseId= input_json['course_id']
    TF= input_json['TF']
    MCQ= input_json['MCQ']
    query = 'EXEC generate_exam ' +str(courseId)+','+ str(TF)+ ','+str(MCQ)
    if 'date' in input_json:
        examExam= input_json['date']
        query = ','+'\''+examExam+'\''

    r = cur.execute(query)
    conn.commit()
    return jsonify({'status': 200, "message":"added"})
    
@app.route('/get_exam_questions', methods=['GET'])
def getQuestionsByExamId():
    input_json = request.get_json(force=True)
    examId = input_json['exam_id']
    query = 'EXEC GetQuestionsByExamId ' + str(examId)
    cur.execute(query)
    r = [dict((cur.description[i][0], str(value))
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'status': 200, "result":r})


@app.route('/store_students_questions', methods=['POST'])
def storeStudentAnswer():
    input_json = request.get_json(force=True)
    examId = input_json['exam_id']
    studentId = input_json['student_id']
    ans_1 = input_json['ans_1']
    ans_2 = input_json['ans_2']
    ans_3 = input_json['ans_3']
    ans_4 = input_json['ans_4']
    ans_5 = input_json['ans_5']
    ans_6 = input_json['ans_6']
    ans_7 = input_json['ans_7']
    ans_8 = input_json['ans_8']
    ans_9 = input_json['ans_9']
    ans_10 = input_json['ans_10']

    query = 'EXEC InsertStudentAnswers ' + str(examId) + ',' + str(studentId) + ',' + '\'' +\
        ans_1 + '\'' + ',' + '\'' + ans_2 + '\'' + ',' + '\'' + ans_3 + '\'' + ',' + '\'' + ans_4 + '\'' + ',' + '\'' +\
            ans_5 + '\'' + ',' + '\'' + ans_6 + '\'' + ',' + '\'' + ans_7 + '\'' + ',' + '\'' + \
                ans_8 + '\'' + ',' + '\'' +\
                ans_9 + '\''+ ',' + '\'' + ans_10 + '\''

    cur.execute(query)
    conn.commit()
    return jsonify({'status': 200, "result":"added"})

@app.route('/correct_student_exam', methods=['POST'])
def correctStudentAnswers():
    input_json = request.get_json(force=True)
    examId = input_json['exam_id']
    studentId = input_json['student_id']
    query = 'EXEC ExamCorrection ' + str(examId) + ',' + str(studentId)
    cur.execute(query)
    conn.commit()
    return jsonify({'status': 200, "result":"corrected"})

