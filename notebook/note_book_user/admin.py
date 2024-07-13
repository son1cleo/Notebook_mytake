from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(NoteBooks)
class NoteBook_Admin(admin.ModelAdmin):
    list_display = [
        'pk','user','date','title','description','image'
    ]