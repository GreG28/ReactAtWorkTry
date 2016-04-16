# Docker pour faire du react et autres, ça serait bien d'explorer
# les possibilité de docker..
FROM debian:jessie
MAINTAINER GreG <gfouillard@cardiweb.com>

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q --fix-missing && apt-get -y -q autoclean && apt-get -y -q autoremove)

EXPOSE 8080

RUN apt-get install -y -q nodejs node npm vim

RUN apt-get update && apt-get install -y -q --fix-missing apt-utils locate

RUN apt-get -y autoclean && apt-get -y autoremove

ENV PATH /usr/local/sbin/bin:$PATH

RUN npm config set prefix /usr/local/sbin

RUN npm install -g webpack

COPY ./dev /usr/local/sbin/reactjsprogramm

RUN cd /usr/local/sbin/reactjsprogramm && npm install

WORKDIR /usr/local/sbin/reactjsprogramm
