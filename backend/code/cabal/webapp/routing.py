from sapp.plugins.pyramid.routing import Routing

from cabal.healthcheck.routing import healthcheck_routing


class CabalWebappRouting(Routing):
    def make(self):
        healthcheck_routing(self)
