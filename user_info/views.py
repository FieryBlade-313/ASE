from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def getUIDByName(username, type="Individual"):
    if type == "Individual" or type == "Organisation":
        try:
            return Individual.objects.get(username=username).UID if type == "Individual" else Organisation.objects.get(username=username).UID
        except:
            return "Username does not exists"
    else:
        return "Invalid Type"


def profile(request, usr_id):
    eth = ['th', 'st', 'nd', 'rd', 'th']
    e = eth[usr_id % 10 if usr_id % 10 < 5 else 0]
    b = render(request, 'user_info/profile.html', {'usr_id': usr_id, 'eth': e})
    b._container[0] = b._container[0]+b._container[0]
    return b


def getUser(request):
    if request.method == 'GET':
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
    if request.method == 'GET':
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
    if request.method == 'POST':
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


@csrf_exempt
def createBulkJob(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        org_uid = str(getUIDByName(
            data['username'], "Organisation")).replace('-', '')
        if org_uid != "Username does not exists" and org_uid != "Invalid Type":
            try:
                bj = BulkJob.objects.create(
                    title=data['title'], noOfEmployees=data['noOfEmployees'], description=data['description'])
                try:
                    OBJ.objects.create(UID_id=org_uid, BID_id=bj.BID)
                    return JsonResponse({"message": "BulkJob created successfully"})
                except:
                    BulkJob.objects.get(BID=bj.BID).delete()
                    return JsonResponse({"message": "BulkJob connector error"})
            except:
                return JsonResponse({"message": "error occured while creating BulkJob"})
        else:
            return JsonResponse({"message": "Unable to find the Organisation"})


@csrf_exempt
def connectBulkJob(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ind_uid = str(getUIDByName(
            data['username'], "Individual")).replace('-', '')
        if ind_uid != "Username does not exists" and ind_uid != "Invalid Type":
            try:
                EBJ.objects.create(UID_id=ind_uid, BID_id=data['BID'])
                return JsonResponse({"message": "Connected with BulkJob successfully"})
            except:
                return JsonResponse({"message": "error occured while connecting with BulkJob"})
        else:
            return JsonResponse({"message": "Unable to find the Individual"})
