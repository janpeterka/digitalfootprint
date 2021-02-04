from app import db

from app.models.base_mixin import BaseMixin


class FacebookComment(db.Model, BaseMixin):
    __tablename__ = "data_facebook_comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    created_by = db.Column(db.ForeignKey("facebook_users.id"), nullable=False)

    author = db.relationship(
        "FacebookUser",
        primaryjoin="FacebookComment.created_by == FacebookUser.id",
        backref="comments",
    )
