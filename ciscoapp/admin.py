from django.contrib.admin import ModelAdmin, register
from ciscoapp.models import *
from django.contrib.admin import AdminSite

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
#from material.admin.decorators import register
#from material.admin.options import MaterialModelAdmin
#from material.admin.sites import site
from django.contrib.auth.models import User, Group
# Register your models here.


admin.site.site_header = 'Solan administration'
admin.site.site_title = 'Solan administration'
admin.site.index_title = 'Solan administration'

class adminT(ModelAdmin):
    site_header = 'Solan administration For Teachers'
    site_title = 'Solan administration'
    index_title = 'Solan administration'
    #register(subject123)
    #register(chapter123)
    
#MaterialModelAdmin = adminT(name='adminT')
#site.register(user)
#site.register(group)
'''
site.register(points)
site.register(login)
site.register(subject123)
site.register(chapter123)
site.register(qotw)

'''
admin.site.register(points)
admin.site.register(login)
admin.site.register(subject123)
admin.site.register(chapter123)
admin.site.register(qotw)
#'''
@register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass
    exclude = ('id',)
