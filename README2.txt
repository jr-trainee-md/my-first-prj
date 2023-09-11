
## switch sqlite -> MariaDB

## install MariaDB server
## run MySQL Client

MariaDB [(none)]> CREATE DATABASE myproject CHARACTER SET UTF8;
MariaDB [(none)]> CREATE USER myuser@localhost IDENTIFIED BY '********';
MariaDB [(none)]> GRANT ALL PRIVILEGES ON myproject.* TO myuser@localhost;
MariaDB [(none)]> FLUSH PRIVILEGES;


PS C:\Users\...> .\venv\Scripts\activate
(venv) PS C:\Users\...> pip install mysqlclient

## some changes in settings.py

+++ """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
+++ """

+++ DATABASES = {
+++     'default': {
+++         'ENGINE': 'django.db.backends.mysql',
+++         'NAME': 'myproject',
+++         'USER': 'myuser',
+++         'PASSWORD': '********',
+++         'HOST': 'localhost',
+++         'PORT': '',
+++     }
+++ }

##

(venv) PS C:\Users\...> cd blogsite
(venv) PS C:\Users\...\blogsite> python manage.py makemigrations
(venv) PS C:\Users\...\blogsite> python manage.py migrate
(venv) PS C:\Users\...\blogsite> python manage.py runserver


