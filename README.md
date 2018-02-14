# Orion

Orion is a Python based application that sends you direct message when someone unfollowed you on Twitter.

## Quick Installation

Spin up a container with your Twitter credentials:

```
docker run -d --name orion --restart=always \
-e USERNAME=<your twitter username> \
-e CONSUMER_KEY=<your consumer key> \
-e CONSUMER_SECRET=<your consumer secret> \
-e ACCESS_TOKEN=<your access token> \
-e ACCESS_SECRET=<your access secret> \
akoken/orion:latest
```

## Build from the ground up

Clone this repo and build image:

```
docker build -t orion:1.0 .
```

Then run the container:


```
docker run -d --name orion --restart=always \
-e USERNAME=<your twitter username> \
-e CONSUMER_KEY=<your consumer key> \
-e CONSUMER_SECRET=<your consumer secret> \
-e ACCESS_TOKEN=<your access token> \
-e ACCESS_SECRET=<your access secret> \
orion:1.0
```

## Kubernetes

If you have a Kubernetes cluster, you can also use deploy.yml file to run the application:

```
kubectl create -f deploy.yml
```
