from db import db

class StudentsModel(db.Model):
    __tablename__ = "students"
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
    
    def get_json(self):
        return {"id": self.id, "name": self.name, "addr": self.addr, "city": self.city, "pin": self.pin}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class StudentScores(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    exam_name = db.Column(db.String(100))
    exam_score = db.Column(db.Integer)

class StudentFees(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    paid_by = db.Column(db.String(100))
    student_fee = db.Column(db.Integer)