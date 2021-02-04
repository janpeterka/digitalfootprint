from app import db

from app.models.base_mixin import BaseMixin


class LocationPoint(db.Model, BaseMixin):
    __tablename__ = "data_location_point"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(Precision=64), nullable=False)
    longitude = db.Column(db.Float(Precision=64), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)

    user = db.relationship(
        "User",
        primaryjoin="LocationPoint.created_by == User.id",
        backref="location_points",
    )
