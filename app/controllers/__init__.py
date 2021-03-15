from .index import IndexView
from .missions import MissionView
from .data_sources.facebook.facebook import FacebookView
from .data_sources.location import LocationView
from .data_sources.messages.messages import MessageView


__all__ = ["IndexView", "MissionView", "FacebookView", "LocationView", "MessageView"]


def register_all_controllers(application):
    IndexView.register(application)
    MissionView.register(application)
    FacebookView.register(application)
    LocationView.register(application)
    MessageView.register(application)


def register_error_handlers(application):
    from .errors import error404
    from .errors import error405
    from .errors import error500

    application.register_error_handler(403, error404)
    application.register_error_handler(404, error404)
    application.register_error_handler(405, error405)
    application.register_error_handler(500, error500)
