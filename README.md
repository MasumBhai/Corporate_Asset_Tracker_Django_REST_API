### Project Name: Corporate Asset Tracker <br/>
#### App name: Asset Tracker

### Project Description:
1. To track corporate assets such as phones, tablets, laptops 
and other gears handed out to employees.
2. The application might be used by several companies
3. Each company might add all or some of its employees
4. Each company and its staff might delegate one or more devices to employees for
 a certain period of time
5. Each company should be able to see when a Device was checked out and returned
6. Each device should have a log of what condition it was handed out and returned

### Project Features:
I have Created a new virtual environment for this project and installed the required packages, which i have shared in requirements.txt file. <br/>
I have used Django Rest Framework for creating the API's. <br/>
I have used SQLITE3 database for this project. <br/>
I have used Django ORM for database operations. <br/>
I have used Django Admin for creating the admin panel. <br/>
I have used Django Serializer for creating the serializers. <br/>
I have used Django Rest Framework Spectacular for creating the API documentation. <br/>
I have used Django Rest Framework Simple JWT for creating the token based authentication. <br/>
I have used python coverage for creating the coverage report. <br/>
I have used Pytest for creating the tests. <br/>
I have used Pytest Factoryboy for creating the factories for Testing. <br/>
I have used Bootstrap Admin for creating the admin dashboard. <br/>
I have used Postman & swagger for testing the API's. <br/>

### Steps to run the project:
1. Clone the project from the git repository. Even you can download the zip file from the git repository. (For your ease: I have included .env file)
    - git clone
2. Create a virtual environment and activate it.
3. Install the required packages from requirements.txt file.
4. Run the following commands:
    - py manage.py makemigrations
    - py manage.py migrate --run-syncdb
    - py manage.py loaddata datadump.json
    - py manage.py createsuperuser
    - py manage.py collectstatic
    - py manage.py runserver
5. Open the browser and hit the following url for performing API testing in swagger:<br/>
   - url: http://127.0.0.1:8000/api/schema/swagger-ui/
6. Now, you have to authenticate yourself before doing any operation. To do that, hit the token endpoint and pass the username and password in the body. You will get a refresh token & access token in the response. Copy the access token and paste it in the authorize section of swagger. Now, you can perform any operation.
7. You can also see the admin dashboard using the following url:
    - url: http://127.0.0.1:8000/admin/
8. Also, you can login to the admin panel using the following / superuser credentials & perform any database operation using my cool admin dashboard panel:
    - username: masum
    - password: masum
    - email: abdullahmasum6035@gmail.com
9. You can also run the tests using the following command:
   - pytest
10. You can also see the coverage report using the following command and open the htmlcov folder & open the index.html file:
    - coverage html
12. You can also see the API documentation using the following url:
    - url: http://127.0.0.1:8000/api/schema/


### Database Schema:





<details><summary><b>Project Commands For Future Use (Geeky Stuff):</b></summary> 

- For secret key generation:
```shell
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```
- For Dumping the data:
```shell
python3 manage.py dumpdata > datadump.json
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
pip install pytest-factoryboy
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
- For Django Admin Dashboard:
```shell
pip install bootstrap-admin
```
- For Database Data Storing:
```shell
py manage.py dumpdata > datadump.json
py manage.py loaddata datadump.json
```
</details>