# base image  
FROM python:3.11

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

WORKDIR /usr/src/app
COPY ./requirements.txt .
# run this command to install all dependencies
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 