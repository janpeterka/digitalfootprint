import datetime
from app import db

from app.models.base_mixin import BaseMixin


class FacebookPost(db.Model, BaseMixin):
    __tablename__ = "facebook_posts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now)

    created_by = db.Column(db.ForeignKey("facebook_users.id"), nullable=False)

    author = db.relationship(
        "FacebookUser",
        primaryjoin="FacebookPost.created_by == FacebookUser.id",
        backref="posts",
    )
