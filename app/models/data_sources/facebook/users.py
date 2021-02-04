from app import db

from app.models.base_mixin import BaseMixin

from flask import url_for


class FacebookUser(db.Model, BaseMixin):
    __tablename__ = "data_facebook_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    profile_picture_path = db.Column(db.String(255), nullable=False)

    @property
    def profile_picture(self):
        picture = type("", (), {})()
        picture.src = url_for("static", filename="images/profile_picture.jpg")
        return picture
