from . import db
import psycopg2


class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    numBeds = db.Column(db.Integer)
    numBath = db.Column(db.Integer)
    location = db.Column(db.String(50))
    price = db.Column(db.Float(2))
    description= db.Column(db.String(225))
    photo = db.Column(db.String(225))
    propertyType = db.Column(db.String(25))

    def __init__(self,title,numBeds,numBaths,location,price,description,photo,propertyType,):
        self.title = title
        self.numBeds = numBeds
        self.location = location
        self.price = price
        self.description = description
        self.photo = photo
        self.propertyType = propertyType

