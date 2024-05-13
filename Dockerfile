FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Create the SQLite database
RUN python3 manage.py create_db

EXPOSE 5000

# CMD ["python3", "manage.py", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "manage:app"]