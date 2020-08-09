FROM node:lts-alpine as base

# install simple http server for serving static content
RUN yarn global add http-server @vue/cli

# make the 'app' folder the current working directory
WORKDIR /code

# install project dependencies
RUN mkdir -p /node_modules && ln -s /node_modules
COPY code/package.json yarn.lock* .
RUN yarn install --dev --ignore-engines --unsafe-perm=true
EXPOSE 8080

FROM base as dev

CMD [ "yarn", "serve", "--host=0.0.0.0" ]

FROM base as build

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY code/ .

# build app for production with minification
RUN yarn run build

# Now set it as an env var
ARG BRANCH=""
ARG COMMIT="dev"
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}
ENV COMMIT_SHA=${COMMIT}
ENV COMMIT_BRANCH=${BRANCH}

EXPOSE 8080
CMD [ "http-server", "../dist" ]
