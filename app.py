from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)   
csrf = CSRFProtect(app)
if __name__ == "__main__":
    from CourseViews import *
    from common import *
    app.run(debug=True)
    csrf.init_app(app)