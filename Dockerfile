FROM python:3.6

EXPOSE 8000

WORKDIR /app

RUN pip install mysql-connector-python

COPY adapters /app/adapters
COPY core /app/core
COPY tests /app/tests
COPY main.py /app
COPY main_sqlite.py /app
COPY main_mysql.py /app
CMD python main_mysql.py 2>&1