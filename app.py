from flask import Flask
import pandas as pd 


app = Flask(__name__)   

if __name__ == "__main__":
    from CourseViews import *
    from common import *
    app.run(debug=True)