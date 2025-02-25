# GCP

## Create GCP Instance

- E2
- e2-micro (2vCPU, 1 core, 1GB memory)
- Allow HTTP
- Allow HTTPS
- Create

## Update

```shell
sudo apt update
sudo apt upgrade -y
```

## Install git

```shell
sudo apt install git -y
```

## Install Docker

https://docs.docker.com/engine/install/debian/

### Setup registry

```shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### Install Docker

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

## Clone repo

```shell
git clone https://github.com/harrelchris/form-api
```

## Start server

```shell
cd ~/form-api
sudo docker compose up -d
```
