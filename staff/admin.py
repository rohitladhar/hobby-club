from django.contrib import admin
from django.contrib.auth.models import Group
from. models import Records, StaffRecords
# Register your models here.

admin.site.site_header="Ladhar Club Admin Dashboard"

admin.site.unregister(Group)
admin.site.register(StaffRecords)