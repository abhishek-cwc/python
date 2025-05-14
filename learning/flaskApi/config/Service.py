#from config.Db import Db
from config.AbstractDb import AbstractDb

class Service:

    @classmethod
    def get(cls,db = AbstractDb):
        print("get exsting connection...")
        return db.getInstance()
    
    @classmethod
    def create(cls, db = AbstractDb):
        print("create new connection...")
        return db.createInstance()

        