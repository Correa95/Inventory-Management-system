# Inventory-Management-system

# Django-Tutorial

<!-- virtual environment setup instruction OR Steps for python Flask

1. py -m venv .venv,  create the virtual environment
2. source .venv/Scripts/activate, activate the virtual environment
3. py -m pip install Django, install Django

py -m pip install -U pip, Install the latest Version of pip

4. To start a project and give it a name: "django-admin startproject myproject"
//////////////////////////
4. To start a project and give it a name: "django-admin startproject myproject" add a "period {.}" stop django from adding an addisional directory

5. Starting the server, py manage.py runserver
6.$ py manage.py startapp api, To create another app or folder for the api models and date

extra:I import django, II print(django.get_version())


<!-- #########command to create DataBase,  py create_db.py -->

<!-- creating and admin user steps
python manage.py createsuperuser
You’ll be prompted to enter:
Username (e.g., admin)
Email address (optional)
Password (you’ll need to confirm it)
Make sure the password meets Django’s complexity requirements. -->

<!-- Resetting and admin user steps
1. python manage.py shell
2. from django.contrib.auth import get_user_model
3. User = get_user_model()
4. User.objects.filter(username="your_admin_username").delete()
5. print("Admin user deleted!") -->
