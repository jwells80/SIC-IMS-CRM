FROM python:latest as base

ENV PYTHONEDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM base as dev
COPY ./requirements-dev.txt /app
RUN pip install -r requirements-dev.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM base as prod
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]