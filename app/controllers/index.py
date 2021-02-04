# from flask import redirect, url_for
from flask import render_template as template

from flask_classful import FlaskView, route


class IndexView(FlaskView):
    route_base = "/"

    def index(self):
        return template("index/index.html.j2")

    @route("about")
    @route("about/")
    @route("o-projektu")
    @route("o-projektu/")
    def about(self):
        return template("index/index.html.j2")

    # @route("terms")
    # def terms(self):
    #     return redirect(url_for("SupportView:terms"))

    # @route("privacy")
    # def privacy(self):
    #     return redirect(url_for("SupportView:privacy"))

    # @route("uptime")
    # def uptime(self):
    #     return "OK"
