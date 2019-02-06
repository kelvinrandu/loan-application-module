# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
    response = json.dumps([{'message': 'welcome'}])
    return HttpResponse(response, content_type='text/json')

# Create your views here.
