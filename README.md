# sendmap git repository

Welcome to the official sendmap.org github repository.
This repository is home to the Django app that runs sendmap.org


## About
sendmap.org is a site designed to map a climber's activity (ticks) climbing areas (crags) around the world.

This is free and open source software developed by Tristan Breetz distributed under the BSD 3-Clause License.

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

![Map Image](https://i.imgur.com/TBjL3Ku.png)

# Installation
## To install locally (linux/unix/macOS/Windows):
1. Ensure Python is installed
2. Ensure Python-pip is installed
3. Install venv through python-pip
4. Run ```git clone https://github.com/tbreetz/sendmap.git ``` in the directory of your choosing
5. Within the newly created ```tickmapper``` directory, execute ```venv env``` to create a new virtual environment
6. (LINUX/UNIX/MACOS ONLY) Run ```source ./env/bin/activate``` to enable the venv
   
   (WINDOWS ONLY) Run ```.\env\Scripts\activate.bat``` to enable the venv
7. ```pip -r ./requirements.txt``` to install needed modules (Django, Requests, etc.)
8. Generate a new database (sqlite, defined in ```./tickmapper/settings.py```) by running ```python manage.py makemigrations``` followed by ```python manage.py migrate```

9. In ```./tickmapper/settings.py```:

      Change ```DEBUG = False``` to ```DEBUG = True```
   
      Change ```allowed_hosts``` to include your hostname/ip address:
      ```
      allowed_hosts = [127.0.0.1, localhost]
      ```
      Disable HTTPS and HSTS settings by commenting out the following lines:
      ```
      # HTTPS settings
      SESSION_COOKIE_SECURE = True
      CSRF_COOKIE_SECURE = True
      SECURE_SSL_REDIRECT = True

      # HSTS settings
      SECURE_HSTS_SECONDS = 31536000 # 1 year
      SECURE_HSTS_PRELOAD = True
      SECURE_HSTS_INCLUDE_SUBDOMAINS = True
      ```
11. Run the app for development ```python manage.py runserver 0.0.0.0:8000```
12. Navigate to http://127.0.0.1/ in a browser (or server IP if remote)
    

## To run once installed:
1. (LINUX/UNIX/MACOS ONLY) Run ```source ./env/bin/activate``` to enable the venv
   
   (WINDOWS ONLY) Run ```.\env\Scripts\activate.bat``` to enable the venv
2. Start server: ```python manage.py runserver 0.0.0.0:8000```
3. Navigate to http://127.0.0.1:8000 in a browser
