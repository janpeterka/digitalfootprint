from app import db

from app.models.base_mixin import BaseMixin


class LocationPoint(db.Model, BaseMixin):
    __tablename__ = "data_location_point"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.ForeignKey("data_users.id"), nullable=False)

    user = db.relationship(
        "User",
        primaryjoin="LocationPoint.user_id == User.id",
        backref="location_points",
    )

    @property
    def name(self):
        return self.created_at
