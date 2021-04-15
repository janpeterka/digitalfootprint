from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms import validators

from flask_wtf import FlaskForm


class FacebookLoginForm(FlaskForm):
    identifier = StringField(
        "Přihlašovací email", [validators.InputRequired("Email musí být vyplněn")]
    )

    real_email = HiddenField()
    real_phone = HiddenField()

    password = PasswordField(
        "Heslo", [validators.InputRequired("Heslo musí být vyplněno")]
    )

    real_password = HiddenField()

    submit = SubmitField("Přihlásit")
