# from flask import redirect, url_for
from flask import request
from flask import render_template as template

from flask_classful import FlaskView

from app.models.missions import Mission

from app import fake


class MissionView(FlaskView):
    def index(self):
        return template("missions/index.html.j2")

    def show(self, id):
        subpage = request.args.get("page", None)

        # mission = Mission.load(id)
        mission = Mission.random_mission()

        if subpage == "info":
            content = template("missions/_info.html.j2", mission=mission)
        elif subpage == "data_browser":
            content = template(
                "data_sources/browser/_browser.html.j2", html=fake.text()
            )

        else:
            content = None

        return template("missions/show.html.j2", mission=mission, content=content)
