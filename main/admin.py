from django.contrib import admin

from .models import *
class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 10

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdmin,]

admin.site.register(Category)
