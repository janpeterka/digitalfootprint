# from flask import redirect, url_for
from flask import render_template as template

from flask_classful import FlaskView, route


from app.models.missions import Mission

class IndexView(FlaskView):
    route_base = "/"

    def index(self):
        first_mission = Mission(id=1)
        return template("index/index.html.j2", mission=first_mission)

    @route("about")
    @route("about/")
    @route("o-projektu")
    @route("o-projektu/")
    def about(self):
        return redirect(url_for("IndexView:index"))

    # @route("terms")
    # def terms(self):
    #     return redirect(url_for("SupportView:terms"))

    # @route("privacy")
    # def privacy(self):
    #     return redirect(url_for("SupportView:privacy"))

    # @route("uptime")
    # def uptime(self):
    #     return "OK"
