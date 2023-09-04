from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/practice'
# app.config['SQL_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
