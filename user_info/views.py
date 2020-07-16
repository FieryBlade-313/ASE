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
    print("-------------------\n", request.GET)
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


def getUserInfo(request):
    print("-------------------\n", request.GET)
    username = request.GET['username']
    type = request.GET['type']
    # print(uid, type)
    if type == 'Individual':
        target = Individual
    elif type == 'Organisation':
        target = Organisation
    else:
        return JsonResponse({'code': 404, 'message': 'Invalid type provided.'})
    try:
        resp = target.objects.get(username=username)
    except target.DoesNotExist:
        return JsonResponse({'code': 404, 'message': 'No entry found.'})
    return JsonResponse(resp.SerializePartial())


# Work Under progress

@csrf_exempt
def register(request):
    # print(request.body)
    data = json.loads(request.body)
    try:
        if data['type'] == 'Individual' or data['type'] == 'Organisation':
            return registerIndividual(data['info']) if data['type'] == 'Individual' else registerOrganisation(data['info'])
        else:
            return JsonResponse({'code': 420, 'message': 'Invalid type provided'})
    except:
        return JsonResponse({'code': 69, 'message': 'Type not provided'})


def registerIndividual(info):
    # save into Individual model
    try:
        Individual.objects.create(username=info['username'], password=info['password'], email=info['email'], contactNo=info["contactNo"], houseNo_flatNo=info["Address"]["houseNo"], street=info["Address"]["street"], landmark=info["Address"]["landmark"], city=info["Address"]["city"], state=info["Address"]
                                  ["state"], country=info["Address"]["country"], pincode=info["Address"]["pincode"], firstName=info["name"]["firstName"], middleName=info["name"]["middleName"], lastName=info["name"]["lastName"], profile_pic=None, DOB=info["DOB"], DOJ=info["DOJ"], age=info["age"], gender=info["gender"])
        return JsonResponse({'message': 'registration successful'})
    except:
        return JsonResponse({'message': 'registration failure'})


def registerOrganisation(info):
    # save into Organisation model
    try:
        Organisation.objects.create(username=info['username'], password=info['password'], email=info['email'], contactNo=info["contactNo"], houseNo_flatNo=info["Address"]["houseNo"], street=info["Address"]["street"], landmark=info["Address"]["landmark"], city=info["Address"]["city"], state=info["Address"]
                                    ["state"], country=info["Address"]["country"], pincode=info["Address"]["pincode"], organisationName=info["organisationName"], organisationLogo=None, description=info["description"])
        return JsonResponse({'message': 'registration successful'})
    except:
        return JsonResponse({'message': 'registration failure'})
