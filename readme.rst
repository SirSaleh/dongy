=====
dongy
=====

dongy is a simple Django app to conduct Web-based sharedcosts calculator.


Quick start
-----------

1. Add "dongycosts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dongycosts',
    ]

2. Include the dongycosts URLconf in your project urls.py like this::

    path('dongycosts/', include('dongycosts.urls')),

3. Run `python manage.py migrate` to create the dongycosts models.

4. (optional) Start the development server and visit http://127.0.0.1:8000/admin/
   to create a dongycost (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/dongycosts/ to participate in the dongycosts.
