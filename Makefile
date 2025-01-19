run:
	poetry run python manage.py runserver
generate_orm:
	poetry run python manage.py inspectdb > models.py
    