# Docker pour faire du react et autres, ça serait bien d'explorer
# les possibilité de docker..
FROM debian:jessie
MAINTAINER GreG <gfouillard@cardiweb.com>

EXPOSE 8080

WORKDIR .


RUN bower install --save react
RUN npm install
