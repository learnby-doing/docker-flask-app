from flask import json, jsonify,request
from flask_restful import Resource, reqparse
from models.students import StudentsModel
from db import db
import json
from utils import get_logger

logger = get_logger(__name__, 'flask_app.log')


class Students(Resource):

    def get(self,name):
        logger.info('*'*100)
        logger.info(f'  <<< getting student details - {name}  >>>')
        students = StudentsModel.find_by_name(name)
        logger.info(f'  {json.dumps(students.get_json(),indent=2)}')
        logger.info('*'*100)
        return students and jsonify(students.get_json())
    
    def post(self, name):
        json_data = request.json
        logger.info('*'*100)
        logger.info(f"  creating student - {name} ")
        logger.info(f'  student details {json.dumps(json_data)}')
        if StudentsModel.find_by_name(name):
            msg = f"⚠️ student {name} already exists!"
            logger.warning(msg)
            return jsonify({"msg":msg})
        db.session.add(StudentsModel(name,**request.json))
        db.session.commit()
        msg = "☑️ inserted successfully!"
        logger.info('*'*100)
        logger.info(msg)
        return jsonify({"msg":msg})

class StudentsAll(Resource):

    def get(self):
        try:
            students = [{"id":student.id,"name":student.name,"city":student.city} for student in StudentsModel.query.all()]
            logger.info("******************** getting all students detail. ********************")
            for student in json.dumps(students,indent=2).splitlines():
                logger.info(student)
            return jsonify(students)
        except Exception as e:
            msg = str(e)
            logger.error(msg)
            return jsonify({"msg":msg})