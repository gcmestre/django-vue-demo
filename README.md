<h2>Install</h2>

Run in the project directory:
```
aptitude install python3-pip
pip install pipenv
pipenv install
```

Before the first starting the server migrations must be applied:
```
python manage.py migrate
```

To run the project:
```
python manage.py runserver
```
