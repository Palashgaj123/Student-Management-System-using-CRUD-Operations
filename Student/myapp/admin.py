from django.contrib import admin
from .models import*
# Register your models here.
@admin.register(stud_data1)
class studentAdmin(admin.ModelAdmin):
    list_display=['RollNo','Name','Email','Department','MobileNo']