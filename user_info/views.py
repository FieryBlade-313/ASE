from django.shortcuts import render
from .models import Individual, Organisation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def profile(request, usr_id):
    eth = ['th', 'st', 'nd', 'rd', 'th']
    e = eth[usr_id % 10 if usr_id % 10 < 5 else 0]
    b = render(request, 'user_info/profile.html', {'usr_id': usr_id, 'eth': e})
    b._container[0] = b._container[0]+b._container[0]
    return b


def getUser(request):
    print("-------------------\n",request.GET)
    uid = request.GET['UID']
    type = request.GET['type']
    # print(uid, type)
    if type == 'Individual':
        target = Individual
    elif type == 'Organisation':
        target = Organisation
    else:
        return JsonResponse({'code': 404, 'message': 'Invalid type provided.'})
    try:
        resp = target.objects.get(UID=uid)
    except target.DoesNotExist:
        return JsonResponse({'code': 404, 'message': 'No entry found.'})
    return JsonResponse(resp.Serialize())


# Work Under progress

@csrf_exempt
def register(request):
    # print(request.body)
    data = json.loads(request.body)
    try:
        if data['type'] == 'Individual' or data['type'] == 'Organisation':
            return registerIndividual(data['info']) if data['type'] == 'Individual' else registerOrganisation(data['info'])
        else:
            return JsonResponse({'code':420,'message':'Invalid type provided'})
    except:
        return JsonResponse({'code':69,'message':'Type not provided'})

def registerIndividual(info):
    #save into Individual model
    return JsonResponse({'type':'Individual'})

def registerOrganisation(info):
    #save into Organisation model
    return JsonResponse({'type':'Organisation'})