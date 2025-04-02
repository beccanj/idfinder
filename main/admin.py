from django.contrib import admin

# Register your models here.
from django.contrib import admin

from main.models import Citizen, RetrievalRequest, LostIDReport

# Register your models here.
admin.site.site_header = 'ID Finder'
admin.site.site_title = 'Manage IDs'


# citizen model
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_id', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'national_id', 'phone_number', 'email')
    list_filter = ('first_name',)
    ordering = ('national_id',)
#Lost_ID
class LostIDReportAdmin(admin.ModelAdmin):
    list_display = ('citizen', 'description', 'location', 'date_reported', 'status')
    search_fields = ('citizen','description', 'location', 'date_reported', 'status')
    list_filter = ('status', 'date_reported')
    ordering = ('-date_reported',)

#Retrieving ID
class RetrievalRequestAdmin(admin.ModelAdmin):
    list_display = ('report', 'citizen', 'request_date', 'status')
    search_fields = ('report', 'citizen', 'request_date', 'status')
    list_filter = ('status', 'request_date')
    ordering = ('-request_date',)

admin.site.register(Citizen, CitizenAdmin)
admin.site.register(LostIDReport, LostIDReportAdmin)
admin.site.register(RetrievalRequest, RetrievalRequestAdmin)

