
# Eclipse Ditto with IPFS

In this project we are mapping the data that is store in Eclipse Ditto to the IPFS


## Getting started

Before running the project you need to setup Eclipse Ditto
  - Docker compose installed

  - Clone Ditto: ```git clone https://github.com/eclipse-ditto/ditto.git```

  - Start Eclipse Ditto following the instructions in https://github.com/eclipse-ditto/ditto

  - Start Eclipse-Ditto-MQTT-iWatch project following the https://github.com/bernar0507/ditto-examples/tree/master/mqtt-iwatch-wot#eclipse-ditto-mqtt-iwatch to populate Eclipse Ditto with some data


## Start project

- Clone the project

```bash
  git clone https://github.com/CamiloPT/Eclipse-Ditto-IPFS.git
```

- Go to the project directory and build the docker image

```bash
  docker build -t ditto-ipfs-image .
```

- Create the docker container for the project

```bash
docker run --name ditto-ipfs --network docker_default ditto-ipfs-image
```

## Run Locally

- Clone the project

```bash
  git clone https://github.com/CamiloPT/Eclipse-Ditto-IPFS.git
```

- Install latest python version

```bash
  sudo apt-get install python3.11 python3-pip python3.11-dev python3.11-venv
```

- Or for MacOS

```bash
  brew install python3.11
```

- Install latest ipfs dameon following the instructions in the following website: https://docs.ipfs.tech/install/ipfs-desktop/#macos


- Create environment

```bash
  python3.11 -m venv env
  source env/bin/activate
```

- Install dependencies

```bash
  pip install -r requirements.txt
```

- Run app

```bash
  python app.py
```
