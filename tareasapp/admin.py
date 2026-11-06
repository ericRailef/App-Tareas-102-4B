from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'completada')  
    search_fields = ('titulo', 'descripcion')     
    list_filter = ('completada',)