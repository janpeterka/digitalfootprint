import datetime
import types

from flask import url_for, abort
from flask import request
from flask import render_template as template

from flask_classful import FlaskView

from app import fake, turbo


from app.models.missions import Mission
from app.models.data_sources.facebook.users import FacebookUser
from app.models.data_sources.facebook.posts import FacebookPost

from app.controllers.data_sources.facebook.facebook import FacebookView


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

        elif subpage == "action_facebook_login":
            print(mission.data_sources["facebook"]["user"])
            content = template(
                "data_sources/browser/_browser.html.j2",
                url="https://facebook.com/login",
                html=FacebookView().login(
                    user=mission.data_sources["facebook"]["user"]
                ),
            )

        else:
            content = None

        return template("missions/show.html.j2", mission=mission, content=content)

    def _load_mission(self, mission_name):
        # WIP - pravděpodobně přesunout do json

        # Password guessing
        if mission_name == "password_guesser":
            # Define mission info
            mission = Mission(
                id=1,
                name="Uhodni heslo",
                info="Uhodni heslo do účtu na sociální sítě na základě veřejně dostupných dat.",
            )

            mission.content = types.SimpleNamespace()

            mission.content.info = mission.info

            # Define data sources
            mission.data_sources = {}
            mission.data_sources["facebook"] = {}
            facebook_user = FacebookUser(
                full_name="Jakub Ryba",
                password="Bramburek99",
                phone_number="+420733264215",
                e_mail="jakub.ryba@seznam.cz",
            )
            facebook_user.posts = [
                FacebookPost(
                    text=f'<img src="{url_for("static", filename="mission_data/password_guesser/photos/birthday_cake.jpg")}"> Nejlepší narozeniny, je mi 22.',
                    created_at=datetime.datetime(2021, 3, 21, 15, 12, 1),
                ),
                FacebookPost.random_post(),
                FacebookPost(
                    text=f'<img src="{url_for("static", filename="mission_data/password_guesser/photos/dog.jpg")}"> Mám psa! Jmenuje se Brambůrek a je rozkošnej.',
                    created_at=datetime.datetime(2020, 12, 6, 10, 13, 56),
                ),
                FacebookPost(
                    text=f"Smazaly se mi kontakty v telefonu, tak pokud chcete, abych si vás přidal, ozvěte se mi na 733264215",
                    created_at=datetime.datetime(2019, 2, 16, 16, 0, 0),
                ),
            ]
            mission.data_sources["facebook"]["user"] = facebook_user

            # Define action pages
            mission.actions = {}
            mission.actions["facebook_login"] = {}

        else:
            abort(404)

        return mission
