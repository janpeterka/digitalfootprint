from app import db

from app.models.base_mixin import BaseMixin

from app.helpers.date_utils import random_datetime


class FacebookComment(db.Model, BaseMixin):
    __tablename__ = "data_facebook_comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    created_by = db.Column(db.ForeignKey("data_facebook_users.id"), nullable=False)

    author = db.relationship(
        "FacebookUser",
        primaryjoin="FacebookComment.created_by == FacebookUser.id",
        backref="comments",
    )

    def random_comment(post):
        import datetime
        import random

        comment = FacebookComment()
        comment.author = post.author
        comment.text = random.choice(  # nosec
            ["Nějaký komentář na facebooku", "Další komentář", "první!"]
        )
        comment.created_at = random_datetime(post.created_at, datetime.datetime.now())

        return comment
