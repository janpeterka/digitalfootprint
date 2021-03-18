from app import db, fake

from app.models.base_mixin import BaseMixin

from app.models.data_sources.facebook.comments import FacebookComment


from app.helpers.date_utils import datetime_days_ago


class FacebookPost(db.Model, BaseMixin):
    __tablename__ = "data_facebook_posts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    created_by = db.Column(db.ForeignKey("data_facebook_users.id"), nullable=False)

    author = db.relationship(
        "FacebookUser",
        primaryjoin="FacebookPost.created_by == FacebookUser.id",
        backref="posts",
    )

    # WIP - only for testing
    @staticmethod
    def random_post(author=None):
        from app.models.data_sources.facebook.users import FacebookUser

        post = FacebookPost()
        post.author = author
        if post.author is None:
            post.author = FacebookUser.random_user()
        post.text = fake.text()
        post.created_at = fake.date_time_between(
            datetime_days_ago(14), datetime_days_ago(1)
        )

        post.comments = [
            FacebookComment.random_comment(post),
            FacebookComment.random_comment(post),
        ]

        return post
