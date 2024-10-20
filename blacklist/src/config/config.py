import os
class Config:
    
    #SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}" 
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ingeniero9!@mydevopsdb.cz6oaaici9tq.us-east-1.rds.amazonaws.com:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

