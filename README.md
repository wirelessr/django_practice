# This repo is the practice with django book.

1. python3 -m virtualenv env_mysite  
2. source env_mysite/bin/activate  
3. django-admin startproject mysite  
4. heroku config:set DJANGO_SETTINGS_MODULE=mysite.production_settings
5. git push heroku master
6. heroku ps:scale web=1
7. heroku run python mysite/manage.py migrate

Now django works on heroku

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
