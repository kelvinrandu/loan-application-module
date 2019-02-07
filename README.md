
[![TypeScript](https://badges.frapsoft.com/typescript/code/typescript.svg?v=101)](https://github.com/ellerbrock/typescript-badges/)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

# loan-application-module
A CRUD application for managing loan applications

## DESCRIPTION
A CRUD application for managing loan applications  built using JavaScript ( Angular6 )  and a REST API written in Python (Django)  forming the backend of the application

## REQUIREMENTS
This project utilizes the listed below stack;
- [Django](https://www.djangoproject.com/)
- [Angular6](https://angular.io/)
- [PostgreSQL](https://www.postgresql.org/)



## TESTING THE APPLICATION
- clone [this](https://github.com/kelvinrandu/loan-application-module.git) repository
- navigate to the root folder andd install virtual environment.
``` $ virtualenv venv```
- activate your virtual environment by typing the command below in your terminal.
``` $ source venv/bin/activate```
- install project dependencies.
``` $ pip install -r requirements.txt```
- to run the backend (Django application) type the code below in your terminal
``` $ python manage.py runserver 127.0.0.1:8000```
- to run the frontend(Angular application) navigate to root folder in django_rest/web/front-end and type the code below in your terminal
``` $ ng serve``

## API ROUTES

| Methods        | Url          | Description |
| ------------- |:-------------:| -----:|
| POST   | http://127.0.0.1:8000/api/personal/    |  create personal info     | 
| POST   | http://127.0.0.1:8000/api/personal/retrieve/  |  retrieve personal info|
| PUT   | http://127.0.0.1:8000/api/personal/update/<int: user_id>/ | update personal info |
| DELETE  |  http://127.0.0.1:8000/api/personal/delete/<int: user_id>/   | personal info |
| POST   | http://127.0.0.1:8000/api/address  |  create address info     | 
| POST   | http://127.0.0.1:8000/api/address/retrieve/  |  retrieve address info|
| PUT   | http://127.0.0.1:8000/api/address/update/<int: address_id>/ | update address info |
| DELETE  |  http://127.0.0.1:8000/api/address/delete/<int: address_id>/   | delete address info |

 
## ENQUIRIES
- for clarifications,enquiries or questions you can contact the developer through randukelvin@gmail.com
