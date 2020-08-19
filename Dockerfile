FROM python:3.7

ADD . /www
WORKDIR /www

ENV SQLITE_PATH '/www/db/dev.db' 
# This will be paseed to uwsgi.ini

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

# RUN apt-get -y update
# RUN apt-get -y upgrade
# RUN apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir /var/log/uwsgi
RUN echo > /var/log/uwsgi/uwsgi.log
CMD uwsgi uwsgi.ini