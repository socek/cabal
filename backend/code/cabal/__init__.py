from cabal.app.app import application


def start_wsgi(settings):
    application.start("default")
    return application.make_wsgi_object()


def start_command(settings):
    application.start("default")
