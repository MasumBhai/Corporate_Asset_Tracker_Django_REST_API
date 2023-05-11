### Project Name: Corporate Asset Tracker <br/>
### App name: Asset Tracker

Created a new virtual environment for this project and installed the required packages, which i have shared in requirements.txt file. <br/>
I have used Django framework for this project. <br/>
I have used Django Rest Framework for creating the API's. <br/>
I have used Postgres database for this project. <br/>
I have used Django ORM for database operations. <br/>
I have used Django Admin for creating the admin panel. <br/>
I have used Django Signals for creating the signals. <br/>

### Steps to run the project:
1. Clone the project from the git repository.
2. Create a virtual environment and activate it.
3. Install the required packages from requirements.txt file.
4. Create a database in postgres and update the database credentials in settings.py file.
5. Run the following commands:
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
6. Open the browser and hit the following url: http://
7. You will see the home page of the project.
8. You can login to the admin panel using the following credentials:
    - username: admin
    - password: admin
    - url: http://
9. You can login to the user panel using the following credentials:


### Project Configuration:
1. Installed the required packages from requirements.txt file.
2. Created a database in postgres and updated the database credentials in settings.py file.
3. Created a superuser using the following command:
    - python manage.py createsuperuser
    - username: admin
    - password: admin
    - email:
4. Created the models for the project.
5. Created the serializers for the project.
6. Created the views for the project.
7. Created the urls for the project.
8. Created the admin panel for the project.
9. Created the user panel for the project.
10. Created the signals for the project.
11. Created the tests for the project.
12. Created the fixtures for the project.
13. Created the API's for the project.
14. Created the documentation for the project.
15. Created the docker file for the project.

### Project Structure:
1. Project Name: corporate_asset_tracker
2. App Name: asset_tracker

### Project API's:
1. Login API:
    - url: http://
    - method: POST
    - body: {"username": "admin", "password": "admin"}
    - response: {"token": "token"}
    - description: This API is used for login to the user panel.
2. Logout API:
3. Forgot Password API:

### Project Commands:
- For secret key generation:
```shell
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```
- For secret key storing:
```shell
pip install python-dotenv
```
- For Rest Framework Support:
```shell
pip install djangorestframework
pip install markdown
pip install django-filter
```
- For API Documentation:
```shell
pip install drf-spectacular
py manage.py spectacular --color --file schema.yml
```
- For Testing:
```shell
pip install coverage
coverage run -m pytest
coverage html
pip install pytest
pip install pytest-django
pytest -h
```
- For superuser creation:
```shell
py manage.py makemigrations
py manage.py migrate
python manage.py createsuperuser
py manage.py runserver
```
- For Token Based Authentication:
```shell
pip install djangorestframework_simplejwt
```

