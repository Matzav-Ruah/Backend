# Run server
rw:
	python web/manage.py runserver

# Migrate
mg:
	python web/manage.py migrate

# Create superuser
cs:
	python web/manage.py createsuperuser

# Makemigrations
mkg:
	python web/manage.py makemigrations