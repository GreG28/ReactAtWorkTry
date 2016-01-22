# Docker pour faire du react et autres, ça serait bien d'explorer
# les possibilité de docker..
FROM debian:jessie
MAINTAINER GreG <gfouillard@cardiweb.com>

ENV localDir ../

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)
RUN apt-get install -y -q apache2 supervisor

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

# RUN mkdir -p /var/log/supervisor
# ADD apache.conf /etc/supervisor/conf.d/apache.conf
# CMD source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND

RUN apt-get install -y -q nodejs npm

RUN npm config set prefix /usr/local

RUN apt-get install -y python python-dev python-pip

RUN pip install flask-restful

RUN npm install -g bower
RUN npm install -g webpack

RUN npm install --save react react-dom

ADD ./* /usr/local/sbin/

WORKDIR /usr/local/sbin

RUN npm install


