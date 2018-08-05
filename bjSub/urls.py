"""bjSub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from bjSub import view

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', view.hello),
=======
    url(r'^$', view.gaodehandle),
>>>>>>> 备注
    path('admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^baiduhandle', view.baiduhandle),
    url(r'^init$', view.init),
    url(r'^stationData$', view.stationData),
    url(r'^POIDetail$', view.POIDetail),
    url(r'^allStation', view.allStation),
    url(r'^stationPOITag', view.stationPOITag),
    url(r'^lostStation', view.lostStation),
    url(r'^stationDetail', view.stationDetail),
    url(r'^gaodehandle', view.gaodehandle),
    url(r'^saveStation$', view.saveStation),
    url(r'^savePoi$', view.savePoi),
    url(r'^stations/$', view.stations),
    url(r'^time/$', view.current_datetime),
<<<<<<< HEAD
    url(r'^time/plus/(\d{1,2})/$', view.hours_ahead)
=======
    url(r'^time/plus/(\d{1,2})/$', view.hours_ahead),
    url(r'^cdBusHandle', view.cdbushandle),
    url(r'^saveBus', view.busHandle),
    url(r'^stationName', view.stationName),
    url(r'^saveGateway', view.saveGateway)
>>>>>>> 备注
]
