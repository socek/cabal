from sapp.plugins.pyramid.views import RestfulView


class HealthcheckView(RestfulView):
    def get(self):
        return {"health": "ok"}
