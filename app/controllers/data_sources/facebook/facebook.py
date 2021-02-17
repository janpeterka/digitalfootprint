from flask import redirect, url_for, request
from flask import render_template as template

from flask_classful import FlaskView, route

from app.helpers.form import create_form, save_form_to_session

from app.models.data_sources.facebook.posts import FacebookPost
from app.models.data_sources.facebook.users import FacebookUser
from app.models.data_sources.facebook.comments import FacebookComment

from app.controllers.data_sources.facebook.forms import FacebookLoginForm


class FacebookView(FlaskView):
    def account(self, id):
        # WIP - for now
        return redirect(url_for("FacebookView:index"))

    def index(self):
        import datetime

        user = FacebookUser(full_name="Jan Peterka")
        user.topics = ["Technology", "Sophie Turner", "Game of Thrones", "TV shows"]

        post = FacebookPost(
            author=user,
            text="Nějaký příspěvek na facebooku",
            created_at=datetime.datetime.today(),
        )

        post1 = FacebookPost(
            author=user, text="Další příspěvek", created_at=datetime.datetime.today(),
        )
        post1.comments = [
            FacebookComment(text="Jóó!", author=user),
            FacebookComment(text="první!", author=user),
        ]

        posts = [post, post1]

        return template(
            "data_sources/facebook/facebook.html.j2", posts=posts, user=user
        )

    def login(self):
        form = create_form(FacebookLoginForm)
        return template("data_sources/facebook/login.html.j2", form=form)

    @route("/login_post", methods=["POST"])
    def login_post(self):
        form = FacebookLoginForm(request.form)

        if not form.validate_on_submit():
            save_form_to_session(request.form)
            return redirect(url_for("FacebookView:login"))
        pass

        user = FacebookUser(full_name="Jan Peterka")
        # user = FacebookUser.load_by_email_or_phone_number(form.email.data)

        if user.check_login(form.password.data):
            return redirect(url_for("FacebookView:account", id=user.id))
        else:
            return redirect(url_for("FacebookView:login"))
