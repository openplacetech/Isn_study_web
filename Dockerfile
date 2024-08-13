# base image
FROM python:3.9.7-buster

# options
ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir core
# set the working directory
# coppy commands
WORKDIR /core

# update docker-iamage packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

# update pip
RUN pip install --upgrade pip
# install python packages
COPY requirements.txt /core/
RUN pip install -r requirements.txt
# create static directory
COPY . /core/

ENV STATIC_ROOT /core/static/
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

EXPOSE 8888
CMD ["gunicorn","--bind", ":8888", "ISNstudy_web.wsgi:application"]
