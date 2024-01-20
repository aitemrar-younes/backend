from django.db import models
from car.models import Car

class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    licence_expiry_date = models.DateField()
    def __str__(self):
        return self.first_name+' '+self.last_name

class Assigned(models.Model):
    account = models.ForeignKey(Account, on_delete = models.PROTECT)
    car = models.ForeignKey(Car, on_delete = models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return f"\"{self.car.matricule}\" assigned to {self.account.last_name} from {self.start_date} to {self.end_date or '-'}"
