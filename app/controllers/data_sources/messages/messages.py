# from flask import redirect, url_for, request, flash
from flask import render_template as template

from flask_classful import FlaskView

# from app.helpers.form import create_form, save_form_to_session

# from app.models.data_sources.messages import Message
from app.models.data_sources.users import User


class MessageView(FlaskView):
    def index(self):
        return template("data_sources/messages/index.html.j2")

    def show_conversation(self, sender=None, reciever=None):
        if not sender:
            sender = User.random_user()
        if not reciever:
            reciever = User.random_user()

        sender.add_sent_messages(reciever)
        reciever.add_sent_messages(sender)

        messages = sender.messages(reciever)
        messages.sort(key=lambda x: (x.created_at))
        # other_user = reciever
        return template(
            "data_sources/messages/feed.html.j2",
            sender=sender,
            reciever=reciever,
            messages=messages,
        )
