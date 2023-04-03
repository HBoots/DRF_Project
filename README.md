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
