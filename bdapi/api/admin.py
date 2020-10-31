from django.contrib import admin
from .models import Human
# Register your models here.

class HumanAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'human_name',
        'human_dob',
        'human_gender',
        'category',
    ]
    readonly_fields= [
        'id',
    ]


admin.site.register(Human,HumanAdmin)
