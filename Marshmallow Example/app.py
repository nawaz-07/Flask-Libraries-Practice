from flask import Flask
from marshmallow import Schema, fields,post_load

app= Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello World'

class BlogPost:
    def __init__(self,id,title,content):
        self.id=id
        self.title=title
        self.content= content

post=BlogPost(id=1,title='Example Post', content='This is my content')
print(post)


class BlogPostSchema(Schema):
      id = fields.Int()
      title=fields.Str()
      content=fields.Str()
      
      @post_load
      def make_blogpost(self,data,**kwargs):
        data['content']=data['content'].upper()
        return BlogPost(**data)


postSchema=BlogPostSchema()
json_data = postSchema.dumps(post)
print(json_data)

load_post=postSchema.loads(json_data)
print(load_post)

if __name__=='__main__':
    app.run(debug=True)