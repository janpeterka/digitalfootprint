from app import db

from app.models.base_mixin import BaseMixin


class User(db.Model, BaseMixin):
    __tablename__ = "data_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)

    @property
    def location_path(self):
        return self.location_points.sort(key=lambda x: (x.created_at))
