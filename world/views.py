# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def index(request):
	now = str(datetime.datetime.now())
	return render_to_response('index.html', {'now': now}, RequestContext(request))

