# django-taskmanager
The repository of django-taskmanager which is a simple task manager

# Information
I started django-taskmanager as a singleuser taskmanger which you can find [here](https://github.com/mmans0ur/django-taskmanager/tree/singleuser)

now it is multiuser


* the groups are defined by website owner
* each user can makes task in the defined groups
* each task has two states Pending and Done
* it works with a query from last three groups

# Usage
you can start with
```
git clone https://github.com/mmans0ur/django-taskmanager.git
```
```
cd django-taskmanager
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```

# Technologies
Django 1.11 + Bootstrap 4.2

# [Requirements](requirements.txt)
