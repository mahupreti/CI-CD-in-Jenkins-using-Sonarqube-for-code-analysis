FROM python:3 
RUN pip install django 
RUN pip install django-ckeditor 
RUN pip install Pillow 

COPY . . 

RUN  python manage.py migrate 


CMD ["python", "manage.py", "runserver","0.0.0.0:6000"]
EXPOSE 6000
