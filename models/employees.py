from db import db

class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
    
    

class EmployeesSalary(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    salary = db.Column(db.Integer)

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin