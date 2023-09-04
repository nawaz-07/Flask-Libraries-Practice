from flask import Flask
from auth.routes import auth_blu
from blog.routes import blog_blu


app=Flask(__name__)

app.register_blueprint(auth_blu)
app.register_blueprint(blog_blu)

if __name__=='__main__':
    app.run(debug=True)