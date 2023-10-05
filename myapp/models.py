from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name + " ( " + str(self.price) + " baht )"

class datauser(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    # price = models.FloatField(default=0.00)
    phone = models.CharField(default=" ", max_length=10)

    def __str__(self):
        # return self.fname + " " + self.lname +  " " + self.address + " ( " + str(self.price) + " baht )"
        return self.fname + " " + self.lname

class customer(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)

    def __str__(self):
        return self.fname + " " + self.lname
    
class buy2(models.Model):
    product = models.CharField(max_length=60)
    price = models.FloatField(default=0.00)
    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.product) + " ( " + str(self.price) + self.name 