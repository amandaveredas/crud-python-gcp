FROM python:3.9.7-alpine

WORKDIR /crud-python-gcp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /crud-python-gcp/
RUN pip install -r requirements.txt

COPY . /crud-python-gcp

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]