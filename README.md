# DJANGO REST FRAMEWORK PROJECT

Follows Winterbottom's Advanced DRF / Docker Udemy course.

```bash
$ sudo docker-compose build

$ sudo docker-compose run --rm app sh -c "django-admin startproject app ."

$ sudo docker-compose up
```

## Dependencies

Django 3.2

Django REST Framework 3.12

## Linting & Testing

Flake8

-   `flake8`

Django Test Suite

-   `python manage.py test`

## Notes

Update `ALLOWED_HOSTS` in `settings.py`.

## Do

-   add Docker Hub credentials to Git Repo

## GITHUB ACTIONS

-   Automation tool (Travis-CI, Jenkins)
-   Automate tasks & run jobs when code changes
    -   Deployment
    -   Linting
    -   Unit Tests

Actions use a shared IP address. The Docker Hub rate limit is used up quickly this way. Authenticate with Docker Hub via auth token through the project 'Actions' section to keep the 200 pull limit applied only to your account.

### Triggers

-   push trigger > job > result (success / fail)
-   2000 free minutes / 6 hours

### Configuration File

`.github/workflows/checks.yml`

### Checking Workflows

Repository > Actions > Name_Of_Config_File

Actions will show success or failure.

## DJANGO TEST FRAMEWORK

Run the test suite...

```bash
$ python manage.py test
```

Built on top of the `unittest` library.

-   Test client (simulated browser)
-   Simulate authentication
-   Temp database

Django REST

-   API test client

### Where To Keep Tests

Use either a test file or a directory inside an app. Not both.

Test file = `tests.py`
Test directory = `tests/`

-   Test modules must start with `test_`
-   Test directory must contain `__init__.py`

### Test Database

Keeps tests out of real database.

Clears data after tests are run. (Can be overridden)

### Test Classes

SimpleTestCase

-   no db
-   save time

TestCase

-   Db
-   most common

```python
from django.test import SimpleTestCase

# import code to test
from . import views

# Create test class
class ViewsTests(SimpleTestCase):
    # Add test methods
    # Setup inputs
    # Execute code
    # Check output with Assertions
    def test():
        pass
```

## DATABASES

-   Add service to `docker-compose.yml`
-   Configure Django for new database in `settings.py`
    -   Engine
    -   Hostname
    -   Port
    -   Database Name
    -   Username
    -   Password

Pull configuration values from env variables.

### Django Database Adapter Package

Psycopg2

-   database adapter package for Django
-   Officially supported by Django

psycopg2-binary

-   not recommended for production
-   not as performant

psycopg2

-   compiles from source
-   compiles specifically for the OS it's running on
-   required dependencies that are not installed by default
-   installs easily with Docker

Finding the correct dependencies can be a chore since they have different names depending on where you look for them.

The psycopg2 documentation list them as:

-   C compilier
-   python3-dev
-   libpq-dev

The equivilant packages for Alpine are:

-   posgtresql-client
-   build-base
-   psotgresql-dev
-   musl-dev

Docker best practice is to clean up build dependencies. The last 3 dependencies above are only required for the initial build so they will be deleted when the build is finished to keep the Docker application as light as possible.
