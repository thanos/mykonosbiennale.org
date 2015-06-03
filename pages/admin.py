from django.contrib import admin
import models 

class PanelInline(admin.TabularInline):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'visible'] 
    model = models.Panel
    extra = 3


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'order', 'slug', 'visible'] 
    search_fields = ['title', 'description_300']
    list_filter = [ 'visible',] 
    list_editable = ['order']
    inlines = [PanelInline]
admin.site.register(models.Page, PageAdmin)    

class PanelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'order', 'slug', 'visible'] 
    search_fields = ['title', 'content']
    list_filter = [ 'visible', 'page'] 
    list_editable = ['order']
admin.site.register(models.Panel, PanelAdmin)