> I took lots of time to study the chapter 11 of django-book. But it is too rough to describe the built-in login/logout; I can even not write a HTML by reading that chapter. So I quit studying django by django-book.  
> I found another tutorial to learn more: https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html. So I will open a new repo to continue.

# This repo is the practice with django book.

1. python3 -m virtualenv env_mysite  
2. source env_mysite/bin/activate  
3. django-admin startproject mysite  
4. heroku config:set DJANGO_SETTINGS_MODULE=mysite.production_settings
5. git push heroku master
6. heroku ps:scale web=1
7. heroku run python mysite/manage.py migrate

Now django works on heroku

# NOTE
The built-in login/logout cannot work for me. I will take some time to study that.

# Studying Notes:
If you want call django packages from external sites, it must setup environments first.

```
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')
import django
django.setup()
```

Template can leverage json

```
inner = {'val':99}
items = {'key':inner}
t = Template('Item 99 is {{ items.key.val }}.')
c = Context({'items':items})
t.render(c)
```

> 'Item 99 is 99.'
