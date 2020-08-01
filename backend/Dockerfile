FROM python:3.8-alpine as base

# Configuration
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    APP_DIR=/code \
    USER_DIR=/home/user \
    PATH=$PATH:/home/user/.poetry/bin

# redis-tools package is required for after deployment tests
RUN apk --update --no-cache add redis postgresql-dev gcc musl-dev curl && \
    pip install --upgrade pip==20.2


# Create dev user
RUN addgroup -S user -g 1000 && adduser -S user -G user -u 1000 && mkdir -p $USER_DIR && chown user:user $USER_DIR && chmod 777 $USER_DIR

# # Create src dir
RUN mkdir -p $APP_DIR && \
    chown user:user $APP_DIR && \
    chmod 777 -R $APP_DIR && \
    mkdir -p /cabal.egg-info && \
    chmod 777 /cabal.egg-info -R && \
    ln -s /cabal.egg-info $APP_DIR/cabal.egg-info
WORKDIR $APP_DIR

USER user
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY --chown=user:user code $APP_DIR
RUN poetry install && poetry run python setup.py develop
CMD /code/start.sh

# Now set it as an env var
ARG BRANCH=""
ARG COMMIT="dev"
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}
ENV COMMIT_SHA=${COMMIT}
ENV COMMIT_BRANCH=${BRANCH}

EXPOSE 8000
