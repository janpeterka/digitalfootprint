from app import db

from app.models.base_mixin import BaseMixin

from flask import url_for


class FacebookUser(db.Model, BaseMixin):
    __tablename__ = "data_facebook_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    profile_picture_path = db.Column(db.String(255), nullable=False)
    topics = db.Column(db.Text)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))

    def _init__(self, **kwargs):
        super().__init__(**kwargs)

        # just for testing purposes
        self.password = "heslo"
        self.phone_number = "+420777777777"

    @staticmethod
    def load_by_email_or_phone_number(identifier):
        FacebookUser.load_by_attribute("email", identifier)
        user = FacebookUser.query.filter_by(email=identifier).first()
        if not user:
            user = FacebookUser.query.filter_by(phone_number=identifier).first()
        return user

    @property
    def profile_picture(self):
        picture = type("", (), {})()
        if self.profile_picture_path:
            picture.src = url_for(
                "static",
                filename=f"data/facebook/users/images/{self.profile_picture_path}.jpg",
            )
        else:
            picture.src = url_for(
                "static", filename="images/profile_picture_placeholder.jpg"
            )
        return picture

    def check_login(self, password):
        return self.password == password

    # @property
    # def topics(self):
    #     return []
