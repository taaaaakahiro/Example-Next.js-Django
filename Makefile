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

migrations:
	${DOCKER} exec web python3 ./backend/manage.py makemigrations

rollback:
	${DOCKER} exec web python3 ./backend/manage.py migrate api_rest_framework zero

show:
	${DOCKER} exec web python3 ./backend/manage.py showmigrations


root:
	${DOCKER} exec web python3 ./backend/manage.py createsuperuser

sh:
	${DOCKER} exec web sh
	

