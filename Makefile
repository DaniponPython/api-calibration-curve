SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )


docker_up:
	docker-compose up -d

docker_up_single:
	docker-compose up -d $(ARG) 

docker_stop:
	docker-compose stop

docker_update_dependencies:
	docker-compose down
	docker-compose up -d --build

docker_test:
	docker-compose run calibration python manage.py test $(ARG) --parallel --keepdb

docker_create_admin_user:
	docker-compose exec calibration python manage.py createsuperuser

docker_migrations:
	docker-compose exec calibration python manage.py makemigrations

docker_logs:
	docker-compose logs -f $(ARG)

docker_migrate:
	docker-compose exec calibration python manage.py migrate

docker_bash:
	docker-compose exec $(ARG) bash

docker_project_permissions:
	docker-compose exec calibration chmod -R 777 .

format:
	black .

flake8_verify:
	flake8 project/


