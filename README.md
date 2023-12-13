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
9. ```pip -r ./requirements.txt``` to install needed modules (Django, Requests, etc.)
10. Generate a new database (sqlite, defined in ```./tickmapper/settings.py```) by running ```python manage.py makemigrations``` followed by ```python manage.py migrate```
11. Run the app during development ```python manage.py runserver 0.0.0.0:8000```
12. Navigate to http://127.0.0.1/ in a browser (or server IP if remote)

    Note: If you are getting errors regarding HTTPS/HSTS/SSL, ensure that you have the relevant lines in ```./tickmapper/settings.py``` removed/commented out (NOT SUITABLE FOR PRODUCTION).

## To run once installed:
1. (LINUX/UNIX/MACOS ONLY) Run ```source ./env/bin/activate``` to enable the venv
   
   (WINDOWS ONLY) Run ```.\env\Scripts\activate.bat``` to enable the venv
2. Start server: ```python manage.py runserver 0.0.0.0:8000```
3. Navigate to http://127.0.0.1:8000 in a browser
