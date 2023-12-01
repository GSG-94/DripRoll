1. Create virtual environment [python -m venv env]
2. Get inside virtual environment [source env/Scripts/activate] Result (env)
    Get out of virtual environment [deactivate]
3. See all packages [pip freeze]
4. Install Django in the virtual environment [pip install django==3.1]
5. Create a new project [django-admin startproject dripRoll .]
6. Create views.py
7. Import views to urls.py
8. Set a path
9. Use Render from django.shortcuts instead of HTTPresponse in views.py
10. Create templates folder
11. In settings.py -> templates -> add in DIRS ['templates']
12. Add static files
13. in setting.py -> STATIC_ROOT
                  -> STATICFILES_DIRS
14. copy static files for webpage [python manage.py collectstatic]
15. Edit HTML files with {% load static %}