### **Objective →**:
To design and build a web application with a configurable pricing module that supports differential pricing by using the Django Admin for the UI.

Procedure:
Create a folder pricing and open with VS code
Create a Python virtual environment: python -m venv venv
Activate the venv: .venv/Scripts/Sctivate.ps1
Create a python Terminal
install django: pip install django
start project using django admin: django-admin startproject pricing
To start server: python manage.py runserver
To migrate: python manage.py migrate
To create admin user: python manage.py createsuperuser

Output:
After running server, check this: http://127.0.0.1:8000/calculate_pricing/
It'll ask values for : distance, time, wit_time, day_of_week
After submit, you'll get the pricing based on the values given.
