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

API Layers
        
    1. Middleware: objectives_dashboard/middleware.py
    2. Routing(REST Layer): objectives_dashboard/urls.py and objectives_dashboard/views.py
    3. Service: objectives_dashboard/service/
    4. DBO: models.py
   
## Other scripts

Data generation scripts
    
    scripts/data.py
#### Usage

This scripts can be used to generate the data for application.

Process of generate the data:
    
    $ python manage.py shell
    
    >>> from scripts.data import dump_data
    
    >>> dump_data()


## Task to be done

    1. Authentication Middleware
    2. API test cases

