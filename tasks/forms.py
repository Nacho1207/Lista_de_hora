from django.forms import ModelForm
from .models import Task

class personnelform(ModelForm):
    class Meta:
        model= Task
        fields= ['apellido_y_nombre', 'jerarquia', 'legajo', 'especialidad', 'importante']