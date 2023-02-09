from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(aboutinfo)
#admin.site.register(product)

@admin.register((aboutinfo))
class aboutinfoModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','subject','messaage']

@admin.register((product))
class productModelAdmin(admin.ModelAdmin):
    list_display=['id','upload_photo','discription']