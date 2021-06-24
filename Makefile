SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )


docker_up:
	docker-compose up -d

docker_up_single:
	docker-compose up -d calibration 

docker_stop:
	docker-compose stop

docker_update_dependencies:
	docker-compose down
	docker-compose up -d --build

docker_test:
	docker-compose run calibration python manage.py test $(ARG) --parallel --keepdb

docker_create_admin_user:
	docker-compose exec calibration python manage.py createsuperuser

docker_makemigrations:
	docker-compose exec calibration python manage.py makemigrations

docker_logs:
	docker-compose logs -f $(ARG)

docker_migrate:
	docker-compose exec calibration python manage.py migrate

test:
	python3 reynolds-number-calculator/manage.py test reynolds-number-calculator/ $(ARG) --parallel --keepdb

format:
	black .


