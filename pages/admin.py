from django.contrib import admin

from .models import Page, Version


class VersionAdmin(admin.ModelAdmin):
    #exclude = ('version',)
    
    class Meta:
        model = Version
        

admin.site.register(Page)
admin.site.register(Version, VersionAdmin)
