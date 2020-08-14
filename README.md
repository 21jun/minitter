# My Flask Application Base Code

## Setup

```sh
pip install -r requirements.txt
```

## Configuration

`config.py`

## Run
```sh
python3 app.py
```



## Docker support

### Build images
```sh
# for Flask App
docker build -t 21jun/flask-base .

# for Nginx Server
cd nginx-docker

docker build -t 21jun/flask-base-nginx .
```

### Run containers

```sh
docker-compose up
# check localhost:80
```