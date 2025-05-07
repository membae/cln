from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata=MetaData()
db=SQLAlchemy(metadata=metadata)


class User(db.Model,SerializerMixin):
    __tablename__="users"
    
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String,nullable=False)
    email=db.Column(db.String,unique=True)
    password=db.Column(db.String, nullable=False)
    role=db.Column(db.String,nullable=False)
    
    
    doctor=db.relationship("Doctor", back_populates="user")
    
 
 
class Doctor(db.Model,SerializerMixin):
    __tablename__="doctors"
    
    id=db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    specialty=db.Column(db.String, nullable=False)
    available=db.Column(db.Boolean, default=True)
    
    user=db.relationship('User',back_populates="doctor")  
    
    