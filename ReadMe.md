Hello World!
Before You Check
NOTE:
1. Change the password of Mysql database in settings.py according to your machine.
2. Makemigrations and migrate

API available:
Provide Token in Auth Token tab
1. http://127.0.0.1:8000/restaurant/
2. http://127.0.0.1:8000/restaurant/menu
3. http://127.0.0.1:8000/restaurant/menu/<int:pk>      (No trailing slash)
4. http://127.0.0.1:8000/restaurant/booking/tables/
5. http://127.0.0.1:8000/restaurant/api-token-auth/    (only Post method from Insomnia)
6. http://127.0.0.1:8000/auth/token/login/             (only Post with username, and password in form)
7. http://127.0.0.1:8000/auth/token/logout/            (only Post with token in auth token tab)
