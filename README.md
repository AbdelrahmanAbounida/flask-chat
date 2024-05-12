# Flask Chat Task
[![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?logo=python)](https://www.python.org/downloads/release/python-360/)



# 0- Installation

```
$ git clone https://github.com/AbdelrahmanAbounida/flask-chat-task
$ cd flask-chat-task
$ pip install -r requirements.txt
```

# 1- .env
Create a .env file in flask-chat-task folder with .env.local fields 

# 2- Create New Database instance

```
$ python3 manage.py create_db
```

# 3- Running

```
$ export FLASK_DEBUG=1
$ export FLASK_APP=manage.py
$ python3 manage.py run
```