from django.contrib import admin

# Register your models here.
from profiles_api import models
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class CategoryResources(resources.ModelResource):
    class Meta:
        model = models.Category

class AutorResources(resources.ModelResource):
    class Meta:
        model = models.Autor


class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','state','creation_date')

    resource_class = CategoryResources





admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Autor)
admin.site.register(models.Post)
