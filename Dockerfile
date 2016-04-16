# Docker pour faire du react et autres, ça serait bien d'explorer
# les possibilité de docker..
FROM debian:jessie
MAINTAINER GreG <gfouillard@cardiweb.com>

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q --fix-missing && apt-get -y -q autoclean && apt-get -y -q autoremove)

EXPOSE 8080 8090

RUN apt-get install -y -q nodejs npm vim

RUN apt-get update && apt-get install -y -q --fix-missing apt-utils python python-dev python-pip locate

RUN apt-get -y autoclean && apt-get -y autoremove

RUN npm config set prefix /usr/local/sbin

RUN pip install flask-restful-swagger flask-cors

RUN npm install -g bower webpack

COPY ./api /usr/local/sbin/api

COPY ./server /usr/local/sbin/server

COPY ./utils/launchReact /etc/init.d/launchReact

RUN chmod ugo+x /etc/init.d/launchReact

RUN update-rc.d launchReact defaults

RUN echo "service launchReact start" >> /root/.bashrc

RUN cd /usr/local/sbin/server && npm install

WORKDIR /usr/local/sbin
