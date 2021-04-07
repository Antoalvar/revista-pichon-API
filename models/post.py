from db import db

class PostModel(db.Model):
    __tablename__ = 'revista_pichon'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(300))

    def __init__(self, post_id, title):
        self.post_id = post_id
        self.title = title

    def json(self):
        return { 'post_id': self.post_id, 'title': self.title }

    @classmethod
    def find_by_id(cls, post_id):
        return cls.query.filter_by(post_id=post_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()