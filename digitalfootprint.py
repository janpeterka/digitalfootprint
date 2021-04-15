import os
import datetime

from app import create_app


env = os.environ.get("FLASK_ENV", "default")
application = create_app(config_name=env)


@application.context_processor
def utility_processor():
    def human_format_date(date):
        time = date.strftime("%H:%M")

        if date == datetime.date.today():
            return f"Dnes v {time}" 
        elif date == datetime.date.today() + datetime.timedelta(days=-1):
            return f"Včera v {time}"
        else:
            return date.strftime("%d.%m.%Y %H:%M")


    return dict(
        human_format_date=human_format_date,
    )

