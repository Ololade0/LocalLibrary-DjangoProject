LOCAL LIBRARY
This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

There are models for books, book copies, genre, language and authors.
Users can view list and detail information for books and authors.
Admin users can create and manage models.

Librarians can renew reserved books
Local Library Model

TO RUN THIS PROJECT FROM LOCAL COMPUTER
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py test 
python3 manage.py createsuperuser 
python3 manage.py runserver
Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
Create a few test objects of each type.
Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
