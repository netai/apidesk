from .views import index


def web_routes(blueprint):
    blueprint.add_url_rule('', endpoint='index', view_func=index, methods=["GET"])
