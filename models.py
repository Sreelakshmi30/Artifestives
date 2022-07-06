from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)


class Category(models.Model):
    category=models.CharField(max_length=50,null=True)

class Club(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categ = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

class User_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    empid=models.CharField(max_length=200, null=True)
    dept=models.CharField(max_length=200, null=True)
    desig=models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    eventname=models.CharField(max_length=200, null=True)
    venue=models.CharField(max_length=200, null=True)
    date=models.CharField(max_length=200, null=True)
    time=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/', null=True)
    status=models.CharField(max_length=200, null=True)


class Albums(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=200, null=True)
    price=models.IntegerField(max_length=200, null=True)

    desc=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/', null=True)
    status=models.CharField(max_length=200, null=True)

class Add_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    payment = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    delivery = models.CharField(max_length=100,null=True)

class Event_Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100,null=True)

class Schedule_time(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    starttime = models.CharField(max_length=100, null=True)
    endtime = models.CharField(max_length=100, null=True)
    practicedate = models.CharField(max_length=100, null=True)
    action=models.CharField(max_length=100, null=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=100, null=True)
    status=models.CharField(max_length=100, null=True)
    action = models.CharField(max_length=50, null=True)


class Talents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    talentname=models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/', null=True)
    status = models.CharField(max_length=200, null=True)

class Competition(models.Model):
    ctname = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=200, null=True)
    ctnumber = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200, null=True)
    status=models.CharField(max_length=200, null=True)
    count=models.IntegerField(max_length=200, null=True)

class Competi_Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100,null=True)