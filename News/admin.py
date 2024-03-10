from django.contrib import admin
from .models import *

from django.utils.html import linebreaks
# Register your models here.


class NewsDetailAdmin(admin.ModelAdmin):
    list_filter = ['author','status']


admin.site.register(NewsDetailModel,NewsDetailAdmin)
admin.site.register(ContactPageModel)
admin.site.register(NewsHomeModel)
admin.site.register(CustomerProfileModel)
admin.site.register(Review)
