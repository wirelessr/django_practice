This repo is the practice with django book.

1. python3 -m virtualenv env_mysite  
2. source env_mysite/bin/activate  
3. django-admin startproject mysite  
4. heroku config:set DJANGO_SETTINGS_MODULE=mysite.production_settings
5. git push heroku master
6. heroku ps:scale web=1
7. heroku run python mysite/manage.py migrate

Now django works on heroku
