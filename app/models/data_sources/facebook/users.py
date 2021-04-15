from app import db, fake

from app.models.base_mixin import BaseMixin

from flask import url_for

from app.models.data_sources.facebook.posts import FacebookPost

# from app.models.data_sources.facebook.comments import FacebookComment


class FacebookUser(db.Model, BaseMixin):
    __tablename__ = "data_facebook_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    profile_picture_path = db.Column(db.String(255), nullable=False)
    topics = db.Column(db.Text)
    password = db.Column(db.String(255))
    e_mail = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))

    # def _init__(self, **kwargs):
    #     super().__init__(**kwargs)

    @staticmethod
    def load_by_email_or_phone_number(identifier):
        user = FacebookUser.load_by_attribute("e_mail", identifier)
        # user = FacebookUser.query.filter_by(e_mail=identifier).first()
        if not user:
            if not identifier[0] == "+":
                identifier = "+420" + identifier
            print(identifier)
            user = FacebookUser.load_by_attribute("phone_number", identifier)
            # user = FacebookUser.query.filter_by(phone_number=identifier).first()
        return user

    @property
    def profile_picture(self):
        picture = type("", (), {})()
        if self.profile_picture_path:
            picture.src = url_for("static", filename=f"{self.profile_picture_path}")
        else:
            picture.src = url_for(
                "static", filename="images/profile_picture_placeholder.jpg"
            )
        return picture

    def check_login(self, password):
        return self.password == password

    # WIP - just for testing purposes
    @staticmethod
    def random_user():
        user = FacebookUser()
        user.id = 1
        user.full_name = fake.name()
        user.password = "heslo"
        user.phone_number = "+420777777777"
        user.topics = [fake.language_name(), fake.name(), fake.job()]

        user.posts = [FacebookPost.random_post(user), FacebookPost.random_post(user)]
        return user
