## some ps commands

PS C:\Users\...> python -m venv venv
PS C:\Users\...> .\venv\Scripts\activate

(venv) PS C:\Users\...> pip install django
(venv) PS C:\Users\...> pip install djangorestframework

(venv) PS C:\Users\...> cd blogsite

(venv) PS C:\Users\...\blogsite> python manage.py makemigrations
(venv) PS C:\Users\...\blogsite> python manage.py migrate

(venv) PS C:\Users\...\blogsite> python manage.py createsuperuser

(venv) PS C:\Users\...\blogsite> python manage.py runserver