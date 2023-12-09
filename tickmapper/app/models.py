from django.db import models

# Create your models here.

class route(models.Model):
    name = models.CharField(max_length=200)
    route_type = models.CharField(max_length=200)
    height = models.IntegerField()
    GPS_lat = models.DecimalField(max_digits=10, decimal_places=6)
    GPS_lon = models.DecimalField(max_digits=10, decimal_places=6)
    grade = models.CharField(max_length = 10)
    def __str__(self):
        return self.name + ":" + self.grade + ":" + self.route_type

class crag(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=20, decimal_places=15)
    lon = models.DecimalField(max_digits=20, decimal_places=15)
    def __str__(self):
        return self.name

class profile(models.Model):
    userName = models.CharField(max_length=200)
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.userName

class tick(models.Model):
    user = models.ForeignKey(profile, on_delete = models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=200)
    route_type = models.CharField(max_length=200)
    height = models.IntegerField()
    grade = models.CharField(max_length = 10)
    crag = models.ForeignKey(crag, on_delete = models.CASCADE)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user','date','name', 'crag'], name="unique ticks")]
    def __str__(self):
        return self.user.userName + ":" + self.name + ":" + self.grade
