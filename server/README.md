# Server

Handles background processes with Flask, Redis Queue, and Docker

### Quick Start

Spin up the containers:

```shell
docker build -t flask-sample-one:latest .
docker run -d -p 5000:5000 flask-sample-one
```

or, if you want to give your container a specific name:

```shell
docker build -t flask-sample-one:latest .
docker run --name my-flask-sample-one -d -p 5000:5000 flask-sample-one
```

Test with:

```

curl "http://localhost:5000/api"

```