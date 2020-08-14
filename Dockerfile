FROM python:3.7

ADD . /www
WORKDIR /www

RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

CMD uwsgi uwsgi.ini