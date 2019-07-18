<h2>Install</h2>

In a linux environment the following is advice to run in the project directory:
```
aptitude install python3-pip
pip install pipenv
pipenv install
```

Before the first run migrations must be applied:
```
python manage.py migrate
```

To run the project:
```
python manage.py runserver
```
