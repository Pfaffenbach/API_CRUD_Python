from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

#Conexao com banco de dados MySQL Workbench
conexao = mysql.connector.connect(host = 'localhost', database = 'youtube', user = 'root', password = 'Ee.46829308')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
db = SQLAlchemy(app)
