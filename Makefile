# Makefile for Django project

PYTHON=python

run:
	$(PYTHON) manage.py runserver

migrate:
	$(PYTHON) manage.py migrate

makemigrations:
	$(PYTHON) manage.py makemigrations

shell:
	$(PYTHON) manage.py shell

createsuperuser:
	$(PYTHON) manage.py createsuperuser

test:
	$(PYTHON) manage.py test

collectstatic:
	$(PYTHON) manage.py collectstatic --noinput

startapp:
	$(PYTHON) manage.py startapp $(name)