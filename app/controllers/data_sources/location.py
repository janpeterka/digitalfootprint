from flask import render_template as template

from flask_classful import FlaskView

from app.models.data_sources.location.points import LocationPoint
from app.models.data_sources.users import User


class LocationView(FlaskView):
    def index(self):
        import datetime
        import random

        user = User(full_name="Jan Peterka")
        points = []
        for i in range(4):
            point = LocationPoint(
                latitude=(14.41 + random.random()),
                longitude=(50.08 + random.random()),
                created_at=datetime.datetime.now(),
                user=user,
            )
            points.append(point)

        points.sort(key=lambda x: (x.created_at))

        return template("data_sources/location/path.html.j2", location_points=points)

    def show(self, id):
        import datetime

        user = User(full_name="Jan Peterka")

        point = LocationPoint(
            latitude=15.2, longitude=56.0, created_at=datetime.datetime.now(), user=user
        )

        return template("data_sources/location/point.html.j2", location_point=point)
