1. Set up system for Django
    1. Create virtual environment [python -m venv env]
    2. Get inside virtual environment [source env/Scripts/activate] Result (env)
        Get out of virtual environment [deactivate]
    3. See all packages [pip freeze]
    4. Install Django in the virtual environment [pip install django==3.1] [python manage.py runserver]
2. Create a new project [django-admin startproject dripRoll .]
3. Create views.py
4. Import views to urls.py
    1. Set a path
5. In views.py
    1. Use Render from django.shortcuts instead of HTTPresponse
6. Create templates folder
7. In settings.py -> templates -> add in DIRS ['templates']
8. Add static files
9. in setting.py -> STATIC_ROOT
                  -> STATICFILES_DIRS
10. copy static files for webpage [python manage.py collectstatic]
11. Edit HTML files with {% load static %}
12. Create Category App [python manage.py startapp category]
    1. Add Category to settings.py
    2. In Category models.py, Create Class
    3. Register Category in admin.py
13. For images install package [pip install pillow]
14. Make migations [python manage.py makemigrations]
15. Run migration [python manage.py migrate]
16. Create Super User [winpty python manage.py createsuperuser]
17. to change from Username to email in Login for Admin 
    1. Create app Accounts [python manage.py startapp accounts]
    2. Add to settings.py 'Accounts'
    3. Write code in accounts -> model.py
    4. Add to settings.py 'AUTH_USER_MODEL'
    5. Register in Account 'Admin.py'
    6. Delete db.sql
    7. Delete Migration files
    8. Run Server to create a new database
    9. Make Migrations [python manage.py makemigrations]
    10. Migrate [python manage.py migrate]
    11. Create Super User [winpty python manage.py createsuperuser]
18. For Uploading Images in settings.py -> MEDIA_URL
                                        -> MEDIA_ROOT
19. 




