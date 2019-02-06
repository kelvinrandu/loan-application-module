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
        return HttpResponse(response, content_type='text/json')
    #     try:

    #         payload = json.loads(request.body)

    #         first_name = payload['first_name']
    #         middle_name = payload['middle_name']
    #         last_name = payload['last_name'] 
    #         id_number = payload['id_number']
    #         email = payload['email']
    #         pin = payload['pin']
    #         marital_status = payload['marital_status']
    #         number_of_dependants = payload['number_of_dependants']

    #         personal_data = User()
    #             first_name=first_name,
    #             middle_name=middle_name
    #             last_name=last_name,
    #             id_number=id_number,
    #             email=email,
    #             pin=pin,
    #             number_of_dependants=number_of_dependants,
    #             marital_status=marital_status    
    #         )

    #         # response = personal_data.create_personal_data()
    #         response = User.me()

            
    #     except :
    #         response = json.dumps([{'message': 'invalid request'}])

    
    # return HttpResponse(response, content_type='text/json')

def employment_details(request):
    response = json.dumps([{'message': 'welcome'}])
    return HttpResponse(response, content_type='text/json')

def loan_details(request):
    response = json.dumps([{'message': 'welcome'}])
    return HttpResponse(response, content_type='text/json')
