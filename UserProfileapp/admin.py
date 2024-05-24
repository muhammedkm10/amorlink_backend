from django.contrib import admin
from .models import BasicDetails,FamilyDetails,LocationDetails,ProfessionalsDetails,ReligionInformation

# Register your models here.
admin.site.register(BasicDetails)
admin.site.register(FamilyDetails)
admin.site.register(LocationDetails)
admin.site.register(ProfessionalsDetails)
admin.site.register(ReligionInformation)

