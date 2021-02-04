from app import db

from app.models.base_mixin import BaseMixin


class FacebookPost(db.Model, BaseMixin):
    __tablename__ = "data_facebook_posts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    created_by = db.Column(db.ForeignKey("facebook_users.id"), nullable=False)

    author = db.relationship(
        "FacebookUser",
        primaryjoin="FacebookPost.created_by == FacebookUser.id",
        backref="posts",
    )
