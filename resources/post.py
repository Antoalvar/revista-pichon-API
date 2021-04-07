from flask_restful import Resource, reqparse
from models.post import PostModel
import psycopg2 as pg2

class Post(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type=str,
        required=True,
        help="Thid field can not left blank"
    )

    def get(self, post_id):
        post = PostModel.find_by_id(post_id)
        if post:
            print(post.json()['post_id'])
            return post.json()

        return {'message': 'post not found'}, 404

    def post(self, post_id):
        if PostModel.find_by_id(post_id):
            return { 'message': "An item with id: '{}' already exist".format(post_id) }, 400

        data = Post.parser.parse_args()
        post = PostModel(post_id, data['title'])

        try:
            post.save_to_db()
        except:
            return {'message': 'An error inserting post'}, 500

        return post.json(), 201

    def delete(self, post_id):
        post = PostModel.find_by_id(post_id)
        if post:
            post.delete_from_db()
            return {'message': f'post with id {post_id} has been deleted'}
        return {'message': 'no post where found to delete'}


    def put(self, post_id):
        data = Post.parser.parse_args()

        post = PostModel.find_by_id(post_id)

        if post is None:
            post = PostModel(post_id, data['title'])
        else:
            post.title = data['title']

        post.save_to_db()
        return post.json()


class PostsList(Resource):
    def get(self):
        print([post.json() for post in PostModel.query.all()])
        return {'posts': [post.json() for post in PostModel.query.all()]}