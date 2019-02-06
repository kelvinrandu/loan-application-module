from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User

import json

def index(request):
    response = json.dumps([{'message': 'welcome'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def personal_details(request):

    if request.method == 'POST':

        try:

            payload = json.loads(request.body)

            first_name = payload['first_name']
            middle_name = payload['middle_name']
            last_name = payload['last_name'] 
            id_number = payload['id_number']
            email = payload['email']
            pin = payload['pin']
            marital_status = payload['marital_status']
            number_of_dependants = payload['number_of_dependants']

            personal_data = User(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                id_number=id_number,
                email=email,
                pin=pin,
                number_of_dependants=number_of_dependants,
                marital_status=marital_status    
            )

            response = personal_data.create_personal_data()
           
            
        except :
            response = json.dumps([{'message': 'invalid request'}])

    
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def retrieve_details(request):

    if request.method == 'POST':

        try:

            payload = json.loads(request.body)
            id_number = payload['id_number']
            user = User.find_by_id(id_number)
            response = json.dumps([{'data': user}])
            
            
        except :
            response = json.dumps([{'message': 'invalid request'}])

    
    return HttpResponse(response, content_type='text/json')



@csrf_exempt
def update_details(request, user_id):

    if request.method == 'PUT':

        try:
            payload = json.loads(request.body)

            first_name = payload['first_name']
            middle_name = payload['middle_name']
            last_name = payload['last_name'] 
            id_number = payload['id_number']
            email = payload['email']
            pin = payload['pin']
            marital_status = payload['marital_status']
            number_of_dependants = payload['number_of_dependants']

            updated_data = User(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                id_number=id_number,
                email=email,
                pin=pin,
                number_of_dependants=number_of_dependants,
                marital_status=marital_status    
            )

            response = updated_data.update_personal_data(user_id)
            
        except :
            response = json.dumps([{'message': 'invalid request'}])

    
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def delete_details(request, user_id):

    if request.method == 'DELETE':

        response = User.delete_personal_data(user_id)

        # try:

        #     response = User.delete_personal_data(user_id)
            
        # except :

        #     response = json.dumps([{'message': 'invalid request'}])

    
    return HttpResponse(response, content_type='text/json')

def employment_details(request):
    response = json.dumps([{'message': 'welcome'}])
    return HttpResponse(response, content_type='text/json')

def loan_details(request):
    response = json.dumps([{'message': 'welcome'}])
    return HttpResponse(response, content_type='text/json')
