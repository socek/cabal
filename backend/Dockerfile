FROM python:3.8-alpine as base

# Configuration
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    APP_DIR=/code \
    USER_DIR=/home/user \
    PATH=/home/user/.poetry/bin:$PATH

# redis-tools package is required for after deployment tests
RUN apk --update --no-cache add redis postgresql-dev gcc musl-dev curl && \
    pip install --upgrade pip==20.2


# Create dev user
RUN addgroup -S user -g 1000 && adduser -S user -G user -u 1000 && mkdir -p $USER_DIR && chown user:user $USER_DIR && chmod 777 $USER_DIR

# # Create src dir
RUN mkdir -p $APP_DIR && \
    chown user:user $APP_DIR && \
    chmod 777 -R $APP_DIR
WORKDIR $APP_DIR

USER user
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# install dependecies
COPY --chown=user:user code/pyproject.toml code/poetry.lock* $APP_DIR
RUN poetry install

# install app
COPY --chown=user:user code/ $APP_DIR
RUN poetry install

CMD /code/start.sh

# Now set it as an env var
COPY --chown=user:user code $APP_DIR
ARG BRANCH=""
ARG COMMIT="dev"
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}
ENV COMMIT_SHA=${COMMIT}
ENV COMMIT_BRANCH=${BRANCH}

EXPOSE 8000
