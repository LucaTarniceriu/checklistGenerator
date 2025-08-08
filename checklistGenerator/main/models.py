from django.db import models

# Create your models here.
class SiteModel(models.Model):
    contract = models.CharField(max_length=30)
    beneficiar = models.CharField(max_length=30)
    locatie = models.CharField(max_length=30)
    nrComanda = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['beneficiar', 'locatie', 'nrComanda'], name='unique_site_location')
        ]

    def __str__(self):
        return self.beneficiar + "_" + self.locatie


class DoorModel(models.Model):
    site = models.ForeignKey(SiteModel, on_delete=models.CASCADE, related_name="doors")

    productType = models.CharField(max_length=30)
    componentNr = models.IntegerField()
    produs = models.CharField(max_length=30)
    anFabricatie = models.IntegerField()
    nr = models.CharField(max_length=30)
    dimensiuni = models.CharField(max_length=30)
    tip = models.CharField(max_length=30)
    titluTabel = models.CharField(max_length=30)

    def __str__(self):
        return self.productType + "(" + self.site.__str__() + ")"

class DoorComponentModel(models.Model):
    door = models.ForeignKey(DoorModel, on_delete=models.CASCADE, related_name="components")

    name = models.CharField(max_length=30)
    broken = models.CharField(max_length=30)
    verified = models.CharField(max_length=30)
    number = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + "<" + self.door.__str__() + ">"