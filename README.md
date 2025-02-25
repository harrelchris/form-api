# form-api

## Requirements

- Python 3
- Docker Desktop

## Development

### Initialize

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp example.env .env
```

### Lint

```shell
ruff format
ruff check --fix
```

### Run

```shell
flask run
```

## Docker

### Build image

```shell
docker build -t app .
```

### Run container

```shell
docker run --detach --publish 8080:8000 --name app --env KEY=1 app
```

### Execute command

```shell
docker exec -it app [your command here]
```

### Access shell

```shell
docker exec -it app bash
```

### Tear down

```shell
docker stop app
docker rm app
docker rmi app
```

## Compose

### Start

```shell
docker compose up -d
```

### Stop

```shell
docker compose down
```
