from django.contrib import admin
from imagekit.admin import AdminThumbnail
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
    list_display = ['title', 'order', 'slug', 'visible', 'slide_show'] 
    search_fields = ['title', 'content']
    list_filter = [ 'visible', 'page'] 
    list_editable = ['order']
admin.site.register(models.Panel, PanelAdmin)


class SlideInline(admin.TabularInline):
    #prepopulated_fields = {"slug": ("title",)}
    fields = ['order', 'title', 'visible', 'image'] 
    list_editable = ['order']
    model = models.Slide
    extra = 10


class SlideShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title',  'slug'] 
    search_fields = ['title', ]
    inlines = [SlideInline]
    save_as = True
admin.site.register(models.SlideShow, SlideShowAdmin)    

class SlideAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("title",)}
    list_display = ['id', 'title', 'order',  'visible', 'image_tag']# 'image_to_use'] 
    #admin_image_to_use = AdminThumbnail(image_field='image_to_use')
    search_fields = ['title', 'content']
    list_filter = [ 'visible', 'slide_show'] 
    list_editable = ['order', 'visible',]
admin.site.register(models.Slide, SlideAdmin)
