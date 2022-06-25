from django.contrib import admin
from .models import Site


# Register your models here.


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name','category','is_available')
    list_filter = ('is_available',)
    prepopulated_fields = {'slug' : ('name',)}
    