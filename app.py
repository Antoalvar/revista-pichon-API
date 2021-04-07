import os

from flask import Flask
from flask_restful import Api
import psycopg2 as pg2

from resources.post import Post, PostsList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:galway@localhost/data')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Post, '/post/<string:post_id>')
api.add_resource(PostsList, '/posts')
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
