from sapp import Decorator
from sapp.plugins.pyramid.views import RestfulView

from cabal import application


class HealthcheckView(RestfulView):
    @Decorator(application, "settings")
    def get(self, settings):
        return {
            "health": "ok",
            "version": settings["version"],
            "git_sha": settings["git_sha"],
            "git_branch": settings["git_branch"],
        }
