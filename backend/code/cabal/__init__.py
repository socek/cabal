from cabal.app.app import application


def wsgi(settings):
    application.start("webapp")
    return application.make_wsgi_object()
