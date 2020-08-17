FROM python:3.7

ADD . /www
WORKDIR /www

RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

RUN sudo apt-get -y update
RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y sqlite3 libsqlite3-dev

CMD uwsgi uwsgi.ini