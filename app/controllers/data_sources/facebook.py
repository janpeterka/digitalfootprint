from flask import render_template as template

from flask_classful import FlaskView

from app.models.data_sources.facebook.posts import FacebookPost
from app.models.data_sources.facebook.users import FacebookUser
from app.models.data_sources.facebook.comments import FacebookComment


class FacebookView(FlaskView):
    def index(self):
        import datetime

        user = FacebookUser(full_name="Jan Peterka")

        posts = []
        post = FacebookPost(
            author=user,
            text="Nějaký příspěvek na facebooku",
            created_at=datetime.datetime.today(),
        )
        posts.append(post)

        post1 = FacebookPost(
            author=user, text="Další příspěvek", created_at=datetime.datetime.today(),
        )
        posts.append(post1)

        comment = FacebookComment(text="Jóó!", author=user)
        post1.comments = [comment]
        return template("data_sources/facebook/facebook.html.j2", posts=posts)
