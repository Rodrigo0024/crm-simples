import os

class Config:
    SECRET_KEY = 'xablau1290'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:geladeira12@localhost/crm_db1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False