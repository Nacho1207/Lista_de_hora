from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'jerarquia', 'legajo', 'especialidad', 'importante', 'turno')


    list_filter = ('importante', 'especialidad', 'turno', 'jerarquia')


    search_fields = ('apellido_y_nombre', 'legajo', 'especialidad')


admin.site.register(Task, TaskAdmin)
