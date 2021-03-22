import datetime
import types

from flask import url_for, abort
from flask import request
from flask import render_template as template

from flask_classful import FlaskView

from app import fake, turbo


from app.models.missions import Mission
from app.models.mission_items import MissionItem
from app.models.data_sources.facebook.users import FacebookUser
from app.models.data_sources.facebook.posts import FacebookPost

from app.controllers.data_sources.facebook.facebook import FacebookView


class MissionView(FlaskView):
    def index(self):
        return template("missions/index.html.j2")

    def show(self, id):
        # mission = Mission.load(id)

        mission = self._load_mission("password_guesser")

        # set contents
        for source in mission.data_sources:
            if source.name == "browser":
                source.html = template(
                    "data_sources/browser/_browser.html.j2", html=fake.text()
                )
            elif source.name == "facebook":
                source.html = FacebookView().show(user=source.user)

        for action in mission.actions:
            if action.name == "facebook_login":
                action.html = FacebookView().login(user=source.user)

        return template("missions/show.html.j2", mission=mission)

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

            # Define data sources
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
            mission.data_sources = [MissionItem(name="facebook", user=facebook_user)]
            # mission.data_sources["facebook"]["user"] = facebook_user

            # Define action pages
            mission.actions = [
                MissionItem(
                    name="facebook_login", human_name="Zadat heslo", user=facebook_user
                )
            ]

        else:
            abort(404)

        return mission
