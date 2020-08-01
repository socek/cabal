#!/usr/bin/env sh

# This is so we can get the commit into the build log of a Dangerfile runner
# These come from https://docs.docker.com/docker-cloud/builds/advanced/

# For debugging all env vars
# printenv

#  Convert the location "/Dockerfile" to "Dockerfile"

docker-compose build --build-arg=COMMIT=$(git rev-parse --short HEAD) --build-arg=BRANCH=$(git branch --show-current)
