# exit on error
set -o errexit

# Navigate to the directory with requirements.txt 
cd ecommerce-backend

# Install dependencies
pip install -r requirements.txt

# Run collectstatic and migrate
python manage.py collectstatic --no-input
python manage.py migrate