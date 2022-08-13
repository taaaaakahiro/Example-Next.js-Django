DOCKER=docker-compose

# docker-compose
build:
	${DOCKER} build

up:
	${DOCKER} up -d

down:
	${DOCKER} down -v

# django/python
test:
	${DOCKER} exec web python3 ./backend/manage.py test

migrate:
	${DOCKER} exec web python3 ./backend/manage.py migrate

migrations:
	${DOCKER} exec web python3 ./backend/manage.py makemigrations

root:
	${DOCKER} exec web python3 ./backend/manage.py createsuperuser

rollback:
	${DOCKER} exec web python3 ./backend/manage.py migrate api_rest_framework zero

sh:
	${DOCKER} exec web sh
	

## Next/React
