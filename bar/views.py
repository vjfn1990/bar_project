import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Beer, Counter, Membership

# Create your views here.

@csrf_exempt
def get_beers(request):
    counter = request.POST.get('counter')
    counters = json.loads(serializers.serialize('json', Counter.objects.filter(name=counter)))
    memberships = json.loads(serializers.serialize('json', Membership.objects.filter(counter=counters[0]['pk'])))
    response = []
    for membership in memberships:
        beer_name = json.loads(serializers.serialize('json', Beer.objects.filter(pk=membership['fields']['beer'])))
        response.append({'name': beer_name[0]['fields']['name'], 'availability': membership['fields']['availability']})
    return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt
def get_counters(request):
    beer = request.POST.get('beer')
    beers = json.loads(serializers.serialize('json', Beer.objects.filter(name=beer)))
    memberships = json.loads(serializers.serialize('json', Membership.objects.filter(beer=beers[0]['pk'])))
    response = []
    for membership in memberships:
        counter_name = json.loads(serializers.serialize('json', Counter.objects.filter(pk=membership['fields']['counter'])))
        response.append({'name': counter_name[0]['fields']['name'], 'availability': membership['fields']['availability']})
    return HttpResponse(json.dumps(response), content_type='application/json')

def index(request):
    return HttpResponse('Index')

def beers(request):
    b = Beer.objects.all()
    context = {'beers': b}
    return render(request, 'bar/beers.html', context)

def counters(request):
    c = Counter.objects.all()
    context = {'counters': c}
    return render(request, 'bar/counters.html', context)
