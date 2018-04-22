# dongycosts app
Django main app for calculation quota of each shared costs per user
## before implement
 to add this file to your website:
 add this lines to your main urls.py
> from django.conf.urls import include
> url(r'^dongycosts/' ,include('dongycosts.urls')),


in `setting.py` add:

>'DIRS': [os.path.join(BASE_DIR, "templates")],
>        'APP_DIRS': True,

and:

>STATIC_ROOT = os.path.join(BASE_DIR, 'static')
>STATIC_URL = '/static/'


>LOGIN_REDIRECT_URL  = '/dongycosts/'
