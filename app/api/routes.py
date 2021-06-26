from .resources import login, register


def api_routes(blueprint):
    blueprint.add_url_rule('/login', endpoint='login', view_func=login, methods=["POST"])
    blueprint.add_url_rule('/register', endpoint='register', view_func=register, methods=["POST"])
