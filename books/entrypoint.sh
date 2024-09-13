#!/bin/sh

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'ddos')" | python manage.py shell || true

python manage.py loaddata books


exec "$@"