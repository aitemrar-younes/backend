from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100, unique=True)
    make = models.ForeignKey(Make, on_delete = models.PROTECT)
    def __str__(self):
        return self.name

class Car(models.Model):
    matricule = models.CharField(max_length=100, unique=True)
    model = models.ForeignKey(Model, on_delete = models.PROTECT)
    def __str__(self):
        return self.matricule
