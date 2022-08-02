DOCKER=docker-compose

build:
	${DOCKER} build

up:
	${DOCKER} up

down:
	${DOCKER} down -v