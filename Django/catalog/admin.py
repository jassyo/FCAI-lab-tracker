from django.contrib import admin

# Register your models here.
from .models import Catalog,Users,Labs,Pcs

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

    
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','jobTitle','userName','password')

class LabsAdmin(admin.ModelAdmin):
    list_display = ('labName','labBuilding','labFNumber','labPcsCount','labChairsCount','labStatus')

class PcsAdmin(admin.ModelAdmin):
    list_display = ('labId','pcStatus','comment')

# Register your models here.

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Labs, LabsAdmin)
admin.site.register(Pcs, PcsAdmin)