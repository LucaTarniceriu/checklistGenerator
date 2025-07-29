from django.contrib import admin
from .models import SiteModel, DoorModel, DoorComponentModel

admin.site.register(SiteModel)
admin.site.register(DoorModel)
admin.site.register(DoorComponentModel)
# Register your models here.

