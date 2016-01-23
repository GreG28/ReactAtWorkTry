# Docker pour faire du react et autres, ça serait bien d'explorer
# les possibilité de docker..
FROM debian:jessie
MAINTAINER GreG <gfouillard@cardiweb.com>

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)

EXPOSE 80

RUN apt-get install -y -q nodejs npm 

RUN apt-get update && apt-get install -y -q --fix-missing python python-dev python-pip

RUN apt-get -y autoclean && apt-get -y autoremove

RUN npm config set prefix /usr/local

RUN pip install flask-restful-swagger

RUN npm install -g bower webpack

ADD ./* /usr/local/sbin/

WORKDIR /usr/local/sbin

RUN npm install
