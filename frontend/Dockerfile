FROM node:lts-buster-slim

RUN npm install -g npm

ADD ./src/package.json ./app/

ADD . ./app

WORKDIR /app

EXPOSE 3000