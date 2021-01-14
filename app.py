from flask import Flask
from flask_cors import CORS
from werkzeug.security import safe_str_cmp
app = Flask(__name__)   
# app.config['SECRET_KEY'] = 'super-secret'
CORS(app)
if __name__ == "__main__":
    from CourseViews import *
    from common import *
    from TopicViews import *
    from QuestionsViews import * 
    from Authentication import * 

    app.run(debug=True)