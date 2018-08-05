import json
from django.http import HttpResponse, Http404

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from bjSub.PoiHandle import PoiHandle
from bjSub.StationHandle import StationHandle
from bjSub.bjsubResponse import ResponseJson, ResponseBad
from bjSub.stationDataHandle import stationDataHandle
from bjSub.POIDetailHandle import POIDetailHandle
<<<<<<< HEAD
=======
from bjSub.GatewayHandle import GatewayHandle
from bjSub.SaveBus import SaveBus
>>>>>>> 备注
from subInfo.models import *
import datetime

def hello(request):
    context = {}
    context['hello'] = '调用百度地图API抓取地铁站周围POI信息'
    return render(request, 'hello.html', context)


def baiduhandle(request):
    return render(request, 'baiduhandle.html')

def gaodehandle(request):
    return render(request,'gaodehandle.html')

<<<<<<< HEAD
=======

def cdbushandle(request):
    return render(request,'cdbushandle.html')

>>>>>>> 备注
def current_datetime(request):
    now = datetime.datetime.now()
    rawhtml = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(rawhtml)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s),it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)



def init(request):
    tags = Tag.objects.all()
    for cur in tags:
        TAGS[cur.name] = cur
    station = Station(name='西二旗')
    station.save()
    st = StationTag(station=station, tag=tags[0])
    st.save()
    return HttpResponse(TAGS)


@csrf_exempt
def stationData(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        stationDataHandle(received_json_data)
        return ResponseJson('ok')
    else:
        return ResponseBad('error')


def allStation(request):
    if request.method == 'GET':
        rsp = []
        all_station = Station.objects.values("id", "name")
        for cur in all_station:
            rsp.append(cur)
        return ResponseJson(rsp)
    else:
        return ResponseBad('error')

def lostStation(request):
    if request.method == 'GET':
        rsp = []
        lost_station = Station.objects.all().filter(state=0).values("id", "name")
        for cur in lost_station:
            rsp.append(cur)
        return ResponseJson(rsp)
    else:
        return ResponseBad('error')

def stationDetail(request):
    if request.method == 'GET':
        rsp = []
        station_info = Station.objects.filter(state=0).values('id', 'name', 'lng', 'lat')

        for cur in station_info:
            cur['point'] = {}
            cur['point']['lng'] = float(cur['lng'])
            cur['point']['lat'] = float(cur['lat'])
            cur.pop('lng')
            cur.pop('lat')
            rsp.append(cur)
        return ResponseJson(rsp)
    else:
        return ResponseBad('error')

<<<<<<< HEAD
=======
def stationName(request):
    if request.method == 'GET':
        rsp=[]
        stationname = Stationname.objects.values('id', 'name')
        for cur in stationname:
            rsp.append(cur['name'])
        return ResponseJson(rsp)
    else:
        return ResponseBad('error')






>>>>>>> 备注

def stationPOITag(request):
    if request.method == 'GET':
        rsp = []
        Tagdata = Tag.objects.values('id', 'name')
        for cur in Tagdata:
            rsp.append(cur)
        return ResponseJson(rsp)
    else:
        return ResponseBad('error')


@csrf_exempt
def POIDetail(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        POIDetailHandle(received_json_data)
        return ResponseJson('ok')
    else:
        return ResponseBad('error')

@csrf_exempt
<<<<<<< HEAD
=======
def busHandle(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        SaveBus(received_json_data)
        return ResponseJson('ok')
    else:
        ResponseBad('error')

@csrf_exempt
>>>>>>> 备注
def saveStation(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        StationHandle(received_json_data)
        return ResponseJson('ok')
    else:
        ResponseBad('error')

@csrf_exempt
<<<<<<< HEAD
=======
def saveGateway(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        GatewayHandle(received_json_data)
        return ResponseJson('ok')
    else:
        ResponseBad('error')

@csrf_exempt
>>>>>>> 备注
def savePoi(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        PoiHandle(received_json_data)
        return ResponseJson('ok')
    else:
        return ResponseBad('error')

def stations(request):
    stationList = Station.objects.all()
    return render(request, 'hello.html', {"stations": stationList})


def ResponseJson(data):
    rsp = {
        'status': 200,
        'data': data
    }
    return HttpResponse(json.dumps(rsp), content_type="application/json")


def ResponseBad(data):
    rsp = {
        'status': 404,
        'data': data
    }
    return HttpResponse(json.dumps(rsp), content_type="application/json")
