
A Simple Django Application
=================================
This application is simple Django application for demonstration of MultiDB Router.

Configuration details for this application
------------------------------------------

To configure this appliction into your local machine you must have installed python, MySql, Postgres and pip package of python.

Once you have installed above requirements then follow these instruction to configure this application.

clone/download this application repository into your local machine.
then navigate to python_test directory and execute the following commands


```
$ pip install -r requirements.txt
```

this will install all required application depandancies.

To install the fake dummy data into the database, firstly you need to create a mentioned databases in respective DBMS

once you created databases then run the following command to load the dummy data in your terminal

```
$ python manage.py loaddata product/fixtures/initial_data.json
```

this command will load the fake data into your database.

To migrate tables in multiple databases use the following command

	python manage.py migrate --database=database1

To start this application just run the following command

    python manage.py runserver

this will start the Django server, you can access the applicaiton on your browser using this url.

	http://localhost:8000/

create a superadmin by using command : python manage.py createsuperuser

Go on admin panel by url : http://localhost:8000/admin
and login by admin credentials to create user with respective database.

By navigating to http://localhost:8000/login, you can access the home page of the application where you can list all the databases that user have subscribed. and also you can create product by selecting subscribed database into the selected database.

Also you can check the list of products in different databases.

To send the mail to the newly created user , please mention the smtp settings in settings.py file.