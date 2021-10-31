# Instructions Development 

## Environment (Windows)

**Reference:** [How to install Django on Windows - Link](https://docs.djangoproject.com/en/3.2/howto/windows/)

```bash
py -m venv bookifly_api_py
bookifly_api_py/Scripts/activate.bat
```

## (optional) Development mode

```bash
python manage.py runserver --settings=bookifly_api_py.settings.dev
```

## Create an administrator

```bash
python manage.py createsuperuser
```