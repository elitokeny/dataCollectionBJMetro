from django.db import models


# Create your models here.

<<<<<<< HEAD
=======
class Stationname(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')

>>>>>>> 备注
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    lng = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    line = models.CharField(max_length=500, default='')
    district = models.CharField(max_length=500, default='')
    center_distance = models.DecimalField(max_digits=10, decimal_places=1,null=True,blank=True)
    state = models.IntegerField()

<<<<<<< HEAD
=======
class Gateway(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, default='')
    lng = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    line = models.CharField(max_length=500, default='')
    district = models.CharField(max_length=500, default='')
    center_distance = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    state = models.IntegerField()


>>>>>>> 备注
# class TagParent(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=500, default='')

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    # parentid = models.ForeignKey(TagParent, on_delete=models.CASCADE)
    # state = models.IntegerField()

class POIDetail(models.Model):
    station = models.ForeignKey(Station,on_delete=models.CASCADE)
    poiname = models.CharField(max_length=500, default='')
    origintag = models.CharField(max_length=500, default='')
    address = models.CharField(max_length=500, default='')
    lng = models.DecimalField(max_digits=10, decimal_places=4)
    lat = models.DecimalField(max_digits=10, decimal_places=4)
    tags = models.CharField(max_length=500, default='')
    distance = models.DecimalField(max_digits=65, decimal_places=4)

class POIDetailTag(models.Model):
    detail = models.ForeignKey(POIDetail, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

<<<<<<< HEAD
=======
# class cdbus(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=500, default='')
#     path = models.CharField(max_length=50000, default='')
#     distance = models.DecimalField(max_digits=65, decimal_places=4)
#     sstop = models.CharField(max_length=500, default='')
#     estop = models.CharField(max_length=500, default='')
#     stime = models.CharField(max_length=500, default='')
#     etime = models.CharField(max_length=500, default='')
#     company = models.CharField(max_length=500, default='')
#     basic_price = models.IntegerField()
#     total_price = models.IntegerField()
#     type = models.CharField(max_length=500, default='')
#     via_stops = models.CharField(max_length=50000, default='')


>>>>>>> 备注
# class LianjiaData(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=500, default='')
#     price = models.IntegerField()
#     address = models.CharField(max_length=500, default='')
#     buildings = models.IntegerField()
#     houses = models.IntegerField()
#     lng = models.DecimalField(max_digits=10, decimal_places=4)
#     lat = models.DecimalField(max_digits=10, decimal_places=4)
#

