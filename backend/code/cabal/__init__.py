from cabal.app.app import application

__version__ = "0.1.0"


def wsgi(settings):
    application.start("webapp")
    return application.make_wsgi_object()
