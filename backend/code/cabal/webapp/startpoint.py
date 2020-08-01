from cabal import app


def webapp(settings):  # settings is dict with configuration from .ini file
    app.start("webapp")
    return app.make_wsgi_object()
