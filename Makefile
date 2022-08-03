DOCKER=docker-compose

build:
	${DOCKER} build

up:
	${DOCKER} up -d

down:
	${DOCKER} down -v

test:
	${DOCKER} exec web python3 ./backend/manage.py test

migrate:
	${DOCKER} exec web python3 ./backend/manage.py migrate

root:
	${DOCKER} exec web python3 ./backend/manage.py createsuperuser

sh:
	${DOCKER} exec web sh
	

