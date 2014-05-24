from django.contrib import admin
from kmeans.models import Info

class InfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['dataset']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    
admin.site.register(Info, InfoAdmin)
