# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run collectstatic and migrate
python manage.py collectstatic --no-input
python manage.py migrate