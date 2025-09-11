from django.db import models
import datetime

# Create your models here.
class SiteModel(models.Model):
    contract = models.CharField(max_length=30)
    beneficiar = models.CharField(max_length=30)
    locatie = models.CharField(max_length=30)
    nrComanda = models.CharField(max_length=30)
    exported = models.BooleanField(default=False)
    oras = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['beneficiar', 'locatie', 'nrComanda'], name='unique_site_location')
        ]

    def __str__(self):
        return self.beneficiar + "_" + self.locatie


class DoorModel(models.Model):
    site = models.ForeignKey(SiteModel, on_delete=models.CASCADE, related_name="doors")
    id = models.AutoField(primary_key=True)

    productType = models.CharField(max_length=30)
    componentNr = models.IntegerField()
    produs = models.CharField(max_length=30)
    anFabricatie = models.IntegerField()
    nr = models.CharField(max_length=30)
    dimensiuni = models.CharField(max_length=30)
    tip = models.CharField(max_length=30, null=True)
    titluTabel = models.CharField(max_length=50, default='')

    nrCanate = models.CharField(max_length=5, default='')
    model = models.CharField(max_length=5, default='', blank=True, null=True)

    dataInspectiei = models.CharField(max_length=11)
    tehnician = models.CharField(max_length=30)

    lipsuri = models.BooleanField(default=False)
    informare = models.BooleanField(default=False)



    def __str__(self):
        return self.produs + " " + self.nr + "(" + self.site.__str__() + ")_" + str(self.id)

class DoorComponentModel(models.Model):
    door = models.ForeignKey(DoorModel, on_delete=models.CASCADE, related_name="components")

    name = models.CharField(max_length=30)
    verified = models.BooleanField(default=True)
    broken = models.BooleanField(default=False)
    number = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    nrcrt = models.IntegerField()

    def __str__(self):
        return str(self.nrcrt) + "<" + self.door.__str__() + ">"