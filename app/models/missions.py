import random
from app import db, fake

from app.models.base_mixin import BaseMixin


class Mission(db.Model, BaseMixin):
    __tablename__ = "missions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    info = db.Column(db.Text, nullable=False)

    # WIP - just for testing purposes
    @staticmethod
    def random_mission():
        return Mission(id=random.randint(1, 200), name=fake.name(), info=fake.text())
