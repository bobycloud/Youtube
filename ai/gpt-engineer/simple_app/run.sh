python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python url_shortener_project/manage.py makemigrations url_shortener
python url_shortener_project/manage.py migrate
python url_shortener_project/manage.py runserver
