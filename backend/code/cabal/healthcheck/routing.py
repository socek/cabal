def healthcheck_routing(routing):
    routing.add("cabal.healthcheck.views.HealthcheckView", "healthcheck", "/")
