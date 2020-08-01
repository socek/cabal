FROM node:lts-alpine as base

# install simple http server for serving static content
RUN yarn global add http-server vue-cli -registry=https://registry.npm.taobao.org

# make the 'app' folder the current working directory
WORKDIR /code

# install project dependencies
COPY code/package.json .
RUN yarn install --dev --ignore-engines --unsafe-perm=true -registry=https://registry.npm.taobao.org --modules-folder=/node_modules
RUN mkdir -p /node_modules && mkdir -p /dist
EXPOSE 8080

FROM base as dev

CMD [ "yarn", "run", "dev", "--host=0.0.0.0" ]

FROM base as build

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY code/ .

# build app for production with minification
RUN yarn run build

EXPOSE 8080
CMD [ "http-server", "../dist" ]
