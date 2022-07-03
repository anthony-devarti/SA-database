from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    method = models.CharField(max_length=200)
    multiplier = models.IntegerField(default=1)

    def __str__(self):
        return self.method
        
class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    total_paid = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    suggested = models.IntegerField()
    delta = models.IntegerField()
    method = models.ForeignKey(Payment, on_delete=models.CASCADE, default=1)
    seller = models.CharField(default="Unknown", max_length=200)
    note = models.CharField(max_length=200)


    def __str__(self):
        return "Order" + str(self.id)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    set_name = models.CharField(max_length=200)
    condition = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    prizeSupport = models.IntegerField(default=0)
    entry = models.IntegerField(default=0)
    registrationLink = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    top8 = models.BooleanField(default=False)
    cap = models.IntegerField(default=0) 


    def __str__(self):
        return self.name + " " + str(self.time)

class Punch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.DateTimeField('date published')
    time_out = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.user.username + " " + str(self.time_in)