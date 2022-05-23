from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Recommendations

# from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def home(request):
    return HttpResponse("Working")

@csrf_exempt
def createRecommendations(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='POST':
        for rec in body_data:
            t = rec['title']
            p = rec['popularity']
            record = Recommendations(title=t,popularity=p)
            record.save()
            return JsonResponse("Done",safe=False)
    return JsonResponse("Failed",safe=False)

@csrf_exempt
def getMostPopular(request):
    if request.method=='GET':
        record = Recommendations.objects.filter(popularity=1)[0]
        print(record.title)
        print(type(record))
        return JsonResponse(record.title,safe=False)

    # print(request)
    # body_unicode = request.body.decode('utf-8')
    # body_data = json.loads(body_unicode)
    # if request.method=='POST':
    #     for rec in body_data:
    #         print(rec)
    #         i = rec['id']
    #         record = Recommendations.objects.get(id=i)
    #         record.delete()
    #         return JsonResponse("Done",safe=False)
    return JsonResponse("Failed",safe=False)

@csrf_exempt
def updateMostPopular(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='POST':
        for rec in body_data:
            print(rec)
            i = rec['id']
            t = rec['title']
            p = rec['popularity']
            record = Recommendations.objects.get(id=i)
            record.title=t
            record.popularity=p
            record.save()
            return JsonResponse("Done",safe=False)
    return JsonResponse("Failed",safe=False)

@csrf_exempt
def deleteMostPopular(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='POST':
        for rec in body_data:
            print(rec)
            i = rec['id']
            record = Recommendations.objects.get(id=i)
            record.delete()
            return JsonResponse("Done",safe=False)
    return JsonResponse("Failed",safe=False)