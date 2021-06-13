import os

DEBUG = True
SECRET_KEY = 'hmmzhdjhsdkajhdkad'  # make sure to change this

SQLALCHEMY_DATABASE_URI = 'mysql://root:'+os.environ.get('sql_password')+'@'+os.environ.get('sql_server')+'/'+os.environ.get('sql_db')
