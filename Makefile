# Run server
rw:
	uv run python web/manage.py runserver

# Migrate
mg:
	uv run python web/manage.py migrate

# Create superuser
cs:
	uv run python web/manage.py createsuperuser

# Makemigrations
mkg:
	uv run python web/manage.py makemigrations