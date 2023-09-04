from flask import Blueprint

auth_blu = Blueprint('auth',__name__)

@auth_blu.route('/login')
def login():
    return 'login page'

@auth_blu.route('/register')
def register():
    return 'Registeration Page'