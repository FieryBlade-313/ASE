from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def getUIDfromBoth(username):
    try:
        return Individual.objects.get(username=username).UID
    except:
        try:
            return Organisation.objects.get(username=username).UID
        except:
            return "No registered user with the given username"


def getUserFromUID(uid):
    try:
        return Individual.objects.get(UID=uid)
    except:
        try:
            return Organisation.objects.get(UID=uid)
        except:
            return "Unable to find"


def getUIDByName(username, type="Individual"):
    if type == "Individual" or type == "Organisation":
        try:
            return Individual.objects.get(username=username).UID if type == "Individual" else Organisation.objects.get(username=username).UID
        except:
            return "Username does not exists"
    else:
        return "Invalid Type"


def getCIDbyName(name):
    try:
        return Category.objects.get(name=name).CID
    except:
        return "No category found"


def profile(request, usr_id):
    eth = ['th', 'st', 'nd', 'rd', 'th']
    e = eth[usr_id % 10 if usr_id % 10 < 5 else 0]
    b = render(request, 'user_info/profile.html', {'usr_id': usr_id, 'eth': e})
    b._container[0] = b._container[0]+b._container[0]
    return b


def getUser(request):
    if request.method == 'GET':
        uid = request.GET['UID']
        resp = getUserFromUID(uid)
        if resp != "Unable to find":
            return JsonResponse(resp.Serialize())
        else:
            return JsonResponse({"message": resp})


def getUserInfo(request):
    if request.method == 'GET':
        uid = request.GET['UID']
        resp = getUserFromUID(uid)
        if resp != "Unable to find":
            return JsonResponse(resp.SerializePartial())
        else:
            return JsonResponse({"message": resp})


def getUserbyType(request):
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


def getUserInfobyType(request):
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
def checkUsernameExists(username):
    try:
        Individual.objects.get(username=username)
        return True
    except:
        try:
            Organisation.objects.get(username=username)
            return True
        except:
            return False


@csrf_exempt
def register(request):
    # print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        if not checkUsernameExists(data['info']['username']):
            try:
                if data['type'] == 'Individual' or data['type'] == 'Organisation':
                    return registerIndividual(data['info']) if data['type'] == 'Individual' else registerOrganisation(data['info'])
                else:
                    return JsonResponse({'code': 420, 'message': 'Invalid type provided'})
            except:
                return JsonResponse({'code': 69, 'message': 'Type not provided'})
        else:
            return JsonResponse({"message": "Username already exists"})


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


def getJobsByCategory(request):
    if request.method == 'GET':
        cat_name = request.GET['cat_name']
        cid = getCIDbyName(cat_name)
        if cid != "No category found":
            try:
                jobs = Jobs.objects.filter(CID_id=cid)
                resp = [a.Serialize() for a in jobs]
                return JsonResponse({'cat_name': cat_name, 'Jobs': resp})
            except:
                return JsonResponse({'message': 'Error while fetching Jobs'})
        else:
            return JsonResponse({'message': 'No category found'})


@csrf_exempt
def login(request):
    data = json.loads(request.body)
    try:
        usr_pass = Individual.objects.get(username=data['username']).password
        return JsonResponse({"message": "login successful"}) if usr_pass == data['password'] else JsonResponse({'message': 'Invalid password'})
    except:
        try:
            usr_pass = Organisation.objects.get(
                username=data['username']).password
            return JsonResponse({"message": "login successful"}) if usr_pass == data['password'] else JsonResponse({'message': 'Invalid password'})
        except:
            return JsonResponse({'message': 'Username not found'})


@csrf_exempt
def review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usr_uid = getUIDfromBoth(data['username'])
        tar_uid = getUIDfromBoth(data['target_username'])
        if usr_uid != "No registered user with the given username" and tar_uid != "No registered user with the given username":
            try:
                rw = Review.objects.create(
                    content=data["content"], rating=data["rating"])
                try:
                    ReviewConnector.objects.create(
                        RID_id=rw.RID, UID=usr_uid, targetID=tar_uid)
                    return JsonResponse({"message": "Review added successfully"})
                except:
                    rw.delete()
                    return JsonResponse({"message": "Error connecting the review"})
            except:
                return JsonResponse({"message": "Error while creating a review"})
        else:
            return JsonResponse({"message": "Invalid username or target_username provided"})
    elif request.method == 'GET':
        return getAllReviews(request)


def getAllReviews(request):
    usr_uid = getUIDfromBoth(
        request.GET['username']) if 'username' in request.GET else None
    tar_uid = getUIDfromBoth(
        request.GET['target_username']) if 'target_username' in request.GET else None
    if usr_uid != "No registered user with the given username" and tar_uid != "No registered user with the given username":
        resp = []
        if usr_uid != None and tar_uid != None:
            resp = ReviewConnector.objects.filter(
                UID=usr_uid, targetID=tar_uid)
        elif usr_uid != None:
            resp = ReviewConnector.objects.filter(UID=usr_uid)
        elif tar_uid != None:
            resp = ReviewConnector.objects.filter(targetID=tar_uid)
        else:
            return JsonResponse({"reviews": resp})

        resp = [a.RID.Serialize() for a in resp]

        return JsonResponse({"reviews": resp})
    else:
        return JsonResponse({"message": "Invalid username or target_username provided"})
