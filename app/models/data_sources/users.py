import random
from app import db, fake

from app.models.base_mixin import BaseMixin

from app.models.data_sources.messages.messages import Message


class User(db.Model, BaseMixin):
    __tablename__ = "data_users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)

    @property
    def location_path(self):
        return self.location_points.sort(key=lambda x: (x.created_at))

    # @property
    def messages(self, penpal):
        messages = []
        # print(self.sent_messages)
        for message in self.sent_messages:
            if message.reciever == penpal:
                messages.append(message)

        for message in self.recieved_messages:
            if message.sender == penpal:
                messages.append(message)

        return messages

    # WIP - just for testing purposes
    @staticmethod
    def random_user():
        return User(id=random.randint(1, 200), full_name=fake.name())

    # WIP - just for testing purposes
    def add_sent_messages(self, reciever, count=random.randint(1, 15)):
        for i in range(count):
            message = Message.random_message(sender=self, reciever=reciever)
