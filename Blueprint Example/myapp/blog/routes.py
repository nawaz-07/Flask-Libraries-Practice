from flask import Blueprint

blog_blu = Blueprint('blog',__name__,url_prefix="/blog")

@blog_blu.route('/')
def index():
    return "Hello Welcome to my Blog"