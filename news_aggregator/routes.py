from news_aggregator.user.view.views import user_registration


def setup_routes(app):
    app.router.add_route('*', '/signin', user_registration)
