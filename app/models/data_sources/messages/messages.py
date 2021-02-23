from app import db, fake
from app.models.base_mixin import BaseMixin

from app.helpers.date_utils import random_datetime, datetime_days_ago

# from app.helpers.random_data import message_texts


class Message(db.Model, BaseMixin):
    __tablename__ = "data_messages"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    created_by = db.Column(db.ForeignKey("data_users.id"), nullable=False)
    sent_to = db.Column(db.ForeignKey("data_users.id"), nullable=False)

    sender = db.relationship(
        "User", primaryjoin="Message.created_by == User.id", backref="sent_messages",
    )

    reciever = db.relationship(
        "User", primaryjoin="Message.sent_to == User.id", backref="recieved_messages",
    )

    # WIP - only for testing
    @staticmethod
    def random_message(sender, reciever):
        message = Message(
            id=1,
            text=fake.text(),
            sender=sender,
            reciever=reciever,
            created_at=random_datetime(datetime_days_ago(14), datetime_days_ago(1)),
        )

        return message
