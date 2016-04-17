from django.contrib import admin
import models 

class VariableAdmin(admin.ModelAdmin):
    list_display = ['key', 'value'] 
    search_fields = ['key', 'value']
    
admin.site.register(models.Variable, VariableAdmin)   