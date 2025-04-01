# exit on error
set -o errexit

pip install -r ecommerce-backend/requirements.txt

# Run collectstatic and migrate
cd ecommerce-backend
python manage.py collectstatic --no-input
python manage.py migrate