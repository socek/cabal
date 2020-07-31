FROM python:3.8-alpine as base

# Configuration
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    APP_DIR=/code \
    USER_DIR=/home/user

# redis-tools package is required for after deployment tests
RUN apk --update --no-cache add redis postgresql-dev gcc musl-dev curl  && \
    pip install pipenv

# Create dev user
RUN addgroup -S user -g 1000 && adduser -S user -G user -u 1000 && mkdir -p $USER_DIR && chown user:user $USER_DIR && chmod 777 $USER_DIR

# Create src dir
WORKDIR $APP_DIR
RUN chmod 777 $APP_DIR

# Install dependencies
COPY --chown=user:user src/Pipfile src/Pipfile.lock src/setup.py $APP_DIR/
RUN pipenv install --dev --system && python setup.py develop

USER user
CMD ./start.sh

FROM base as main
# Copy all the src and run setuo.py
COPY --chown=user:user src $APP_DIR

EXPOSE 18765
