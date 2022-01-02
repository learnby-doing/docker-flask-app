import json
import logging

from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,reqparse, Resource
from resources.students import Students, StudentsAll

from utils import get_logger

app = Flask(__name__)
# database_uri = f"mysql+pymysql://root:my-secret-pw@localhost:3306/flask"
database_uri = f"sqlite:///app.db"
app.config["SQLALCHEMY_DATABASE_URI"]=database_uri
api = Api(app)

logger = get_logger(__name__, "flask_app.log")

@app.before_first_request
def create_db():
    logging.info("    <<<<<<<<<<<  Creating DB    >>>>>>>>>>>>>")
    db.create_all()
    logging.info("         DB created Successfully!       " )

api.add_resource(StudentsAll,"/students")
api.add_resource(Students,"/student/<string:name>")

if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=3030,debug=True)