# exit on error
set -o errexit

# Install dependencies - path needs to be explicit since we're running from repo root
pip install -r ecommerce-backend/requirements.txt

# Run collectstatic and migrate
cd ecommerce-backend
python manage.py collectstatic --no-input
python manage.py migrate