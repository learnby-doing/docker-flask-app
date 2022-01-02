from db import db

def get_table_from_db(table_name):
    return db.Table(table_name,db.metadata,autoload=True,autoload_with=db.engine)