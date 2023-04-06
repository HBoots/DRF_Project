# CREATING USER MODELS

Make custom model classes based upon some of Django's user model classes then customize to suit.

`BaseUserManager` provides functionality in creating and managing users.

`AbstractBaseUser` is the standard user model in Django.

Create a custom user manager and a custom user model. Set a property of the user model to an instance of the user manager.

```python
objects = UserManager()
```

- Then use the `get_user_model()` method to get the current user model. This is useful if the user model changes and changes its name. The method will always find the current user model.
- Call the attribute in the user model that calls the user manager.
- Call any user management methods (e.g. `create_user()`) from the attribute

```python
get_user_model().objects.create_user()
```

- Set the `AUTH_USER_MODEL` variable in `settings.py` to the app and user model.

```python
AUTH_USER_MODEL  = 'core.User'
```
