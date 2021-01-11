from flask import Flask
from flask_cors import CORS

app = Flask(__name__)   
CORS(app)
if __name__ == "__main__":
    from CourseViews import *
    from common import *
    from TopicViews import *
    app.run(debug=True)
