# Objectives Summary APIs

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv -p python3.6 venv 
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

## Code base Details

### API Layers
        
    1. Middleware: objectives_dashboard/middleware.py
    2. Routing(REST): objectives_dashboard/urls.py and objectives_dashboard/views.py
    3. Service: objectives_dashboard/service/
    4. DBO: models.py
   
### Other scripts

Data generation scripts
    
    scripts/data.py
    
This scripts can be used to generate the dummy data for application.

## Database details

By default its pointing to sqlite database which is pushed to the repo, 
but we can connect to postgres database by providing exporting the details in `.env_sample` 
and run following command,

    $ export $(xargs < .env_sample)
    $ python manage.py runserver

once the database is connection is done, run following commands to create tables and relationships, 

    $ python manage.py makemigrations
    $ python manage.py migrate


Dummy data can be created using the script provided, The usage as below,
    
    $ python manage.py shell
    >>> from scripts.data import dump_data    
    >>> dump_data()


### Postman

[Collection Link](https://www.getpostman.com/collections/15740f56c5ca67052a57)



## Task to be done

    1. Authentication
    2. API unittests
