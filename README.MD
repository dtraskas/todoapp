# Basic TODO App 

This is a basic TODO app, that can be deployed using the included Helm charts on Kubernetes. First you should set up a Kubernetes cluster with the repo found [here](https://github.com/dtraskas/dev-cluster1). 

The app can only store todo items in memory and offers three endpoints:

```http
GET /healthz
POST /tasks
GET /tasks
```

The `healthz` endpoint is used by Kubernetes to check the deployed pods for their health.

## Prerequisites to run locally

- Docker installed
- A Docker container registry to push the App image which you will have to replace in the Makefile

To run locally simply execute:

```bash
export FLASK_APP=app
flask run
```

## Prerequisites to deploy on Kubernetes

As mentioned earler, you will first need to provision a Kubernetes cluster or have one already running. 

You then to need to have:

- Helm installed
- An already provisioned Elastic Load Balancer on AWS by creating an NGINX Ingress Controller

To deploy on Kubernetes from the root execute:

```bash
helm install todoapp deployment/todoapp/ -f deployment/prod-values.yaml 
```