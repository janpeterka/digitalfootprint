from flask import redirect, url_for, request, flash
from flask import render_template as template

from flask_classful import FlaskView, route

# from app import turbo

from app.helpers.form import create_form  # , save_form_to_session

# from app.models.data_sources.facebook.posts import FacebookPost
from app.models.data_sources.facebook.users import FacebookUser

# from app.models.data_sources.facebook.comments import FacebookComment

from app.controllers.data_sources.facebook.forms import FacebookLoginForm


class FacebookView(FlaskView):
    def account(self, id):
        # WIP - for now
        return redirect(url_for("FacebookView:index"))

    def show(self, user):
        if not user:
            user = FacebookUser.random_user()

        return template(
            "data_sources/facebook/_facebook.html.j2",
            posts=user.posts,
            user=user,
            with_about=False,
        )

    def login(self, user=None):
        form = create_form(FacebookLoginForm)
        form.real_password.data = user.password
        form.real_email.data = user.e_mail
        form.real_phone.data = user.phone_number
        return template("data_sources/facebook/_login.html.j2", form=form, user=user)

    # @route("/login_post_AJAX", methods=["POST"])
    # def login_post_check_AJAX(self):
    #     form = FacebookLoginForm(request.form)

    #     print(request)

    #     if not form.validate_on_submit():
    #         flash("Špatně vyplněný formulář")
    #         # return redirect

    #     # user = FacebookUser.load_by_email_or_phone_number(form.username.data)

    #         # if not identifier[0] == "+":
    #         #     identifier = "+420" + identifier
    #         # print(identifier)
    #         # user = FacebookUser.load_by_attribute("phone_number", identifier)

    #     # validate email
    #     if form.identifier.data == form.real_email.data:
    #         validation = True

    #     elif form.identifier.data == form.real_phone.data:
    #         validation = True

    #     elif ("+420" + form.identifier.data) == form.real_phone.data:
    #         validation = True

    #     else:
    #         validation = False


    #     if validation and form.password.data == form.real_password.data:
    #         print(request)
    #         # return redirect()
            
    #     else:
    #         print("špatné heslo")
    #         flash("Špatně zadané heslo")
    #         # return False

        # return 
