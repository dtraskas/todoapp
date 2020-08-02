REGISTRY=430153336777.dkr.ecr.eu-west-2.amazonaws.com
VERSION ?= latest
IMAGE_NAME ?= todoapp
CONTAINER_NAME ?= todoapp
CONTAINER_INSTANCE ?= default

.PHONY: build tag push release

build: 	Dockerfile
	docker build -t $(IMAGE_NAME):$(VERSION) -f Dockerfile .

tag:
	docker tag $(IMAGE_NAME):$(VERSION) $(REGISTRY)/$(IMAGE_NAME):$(VERSION)

push:
	docker push $(REGISTRY)/$(IMAGE_NAME):$(VERSION)

release: build
	make push -e VERSION=$(VERSION)
    
default: build