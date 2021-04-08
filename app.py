import os

from flask import Flask
from flask_restful import Api
import psycopg2 as pg2
from db import db

from resources.post import Post, PostsList

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kpzeepxbsthjgz:a7b1e2edf861ad5b9f6e550d11992dbb186872c8a0eb59a610f5fa0f37b4eedc@ec2-54-228-99-58.eu-west-1.compute.amazonaws.com:5432/d4b5r8scgi7932'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api.add_resource(Post, '/post/<string:post_id>')
api.add_resource(PostsList, '/posts')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
