from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
db = SQLAlchemy()



class Blacklist(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    app_uuid = db.Column(db.String(36), nullable=False)
    blocked_reason = db.Column(db.String(255))
    ip_address = db.Column(db.String(45))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Blacklist
         load_instance = True