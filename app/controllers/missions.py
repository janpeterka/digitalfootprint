import datetime

from flask import url_for, abort
from flask import request
from flask import render_template as template

from flask_classful import FlaskView

from app.models.missions import Mission
from app.models.data_sources.facebook.users import FacebookUser
from app.models.data_sources.facebook.posts import FacebookPost

from app import fake


class MissionView(FlaskView):
    def index(self):
        return template("missions/index.html.j2")

    def show(self, id):
        subpage = request.args.get("page", None)

        # mission = Mission.load(id)

        mission = self._load_mission("password_guesser")

        if subpage == "info":
            content = template("missions/_info.html.j2", mission=mission)
        elif subpage == "data_browser":
            content = template(
                "data_sources/browser/_browser.html.j2", html=fake.text()
            )
        elif subpage == "data_facebook":
            content = template(
                "data_sources/facebook/_facebook.html.j2",
                user=mission.data_sources["facebook"]["user"],
            )

        else:
            content = None

        return template("missions/show.html.j2", mission=mission, content=content)

    def _load_mission(self, mission_name):
        # Password guessing
        if mission_name == "password_guesser":
            # Define mission info
            mission = Mission(
                id=1,
                name="Uhodni heslo",
                info="Uhodni heslo do účtu na sociální sítě na základě veřejně dostupných dat.",
            )

            # Define data sources
            mission.data_sources = {}
            mission.data_sources["facebook"] = {}
            facebook_user = FacebookUser(full_name="Jakub Ryba")
            facebook_user.posts = [
                FacebookPost(
                    text=f'<img src="{url_for("static", filename="mission_data/password_guesser/photos/birthday_cake.jpg")}"> Nejlepší narozeniny',
                    created_at=datetime.datetime(2021, 3, 21, 15, 12, 1),
                ),
                FacebookPost.random_post(),
                FacebookPost(
                    text=f'<img src="{url_for("static", filename="mission_data/password_guesser/photos/dog.jpg")}"> Mám psa!',
                    created_at=datetime.datetime(2020, 12, 6, 10, 13, 56),
                ),
            ]
            mission.data_sources["facebook"]["user"] = facebook_user

            # Define action pages

        else:
            abort(404)

        return mission
