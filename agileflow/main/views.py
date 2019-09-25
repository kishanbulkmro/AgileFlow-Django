from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , render_to_response
import pandas as pd
from django.db import transaction


# Create your controller here.

@transaction.atomic
def index(request):
    return render_to_response('inquiry.html')