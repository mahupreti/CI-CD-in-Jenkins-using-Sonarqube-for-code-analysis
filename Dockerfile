FROM python:3 
RUN pip install django 
RUN pip install django-ckeditor 
RUN pip install Pillow 

COPY . . 

RUN  python manage.py migrate 
EXPOSE 3000 

CMD ["python", "manage.py", "runserver","127.0.0.1:3000"]
