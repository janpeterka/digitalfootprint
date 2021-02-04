from flask import url_for
from flask import render_template as template

from flask_classful import FlaskView


class FacebookView(FlaskView):
    def index(self):
        import datetime
        import copy

        posts = []
        post = type("", (), {})()
        post.author = type("", (), {})()
        post.author.profile_picture = type("", (), {})()
        post.author.profile_picture.src = url_for(
            "static", filename="images/profile_picture.jpg"
        )
        post.author.full_name = "Jan Peterka"
        post.text = "Nějaký příspěvek na facebooku"
        post.created_at = datetime.datetime.today()
        posts.append(post)
        post1 = copy.deepcopy(post)
        post1.text = "Další příspěvek"
        posts.append(post1)
        return template("data_sources/facebook/facebook.html.j2", posts=posts)
