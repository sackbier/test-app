from django.db import models

class Drone(models.Model):
    drone_model = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    camera = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.drone_model

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Case(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    billing_days = models.IntegerField()
    drone = models.ForeignKey(Drone)
    customer = models.ForeignKey(Customer)
    status = models.CharField(max_length=20, choices=[('iq', 'inquiry'), ('bk', 'booked'), ('cn', 'cancelled'), ('bl', 'billed'), ('pd', 'payed')], default='bk')

    def __str__(self):
        t = self.start_date.strftime('%d/%m/%Y') + ' - ' + self.end_date.strftime('%d/%m/%Y')
        return t

    def _get_price(self):
        return self.billing_days * self.drone.price
    price = property(_get_price)