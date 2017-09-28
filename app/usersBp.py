from flask import Blueprint, json, request
import requests

from app import db
from .models import  User

userRoutes = Blueprint('users', __name__)

@userRoutes.route('/create', methods=['POST'])
def createUser():
	return

@userRoutes.route('/info', methods=['POST'])
def getInfo():
	return

@userRoutes.route('/edit', methods=['POST'])
def editInfo():
	return

@userRoutes.route('/delete', methods=['POST'])
def deleteUser():
	return
