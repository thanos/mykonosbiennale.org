from django.contrib import admin
import models 


class FestivalAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', ]   
admin.site.register(models.Festival, FestivalAdmin)  



class ArtAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['photo', 'title', 'description', 'text']   
    search_fields = ['title', 'description','text']
admin.site.register(models.Art, ArtAdmin)        



 
class ArtInline(admin.TabularInline):
    model = models.Art
    extra = 3
    
class ArtistAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'email', 'homepage', 'country','festival','event','visible']
    search_fields = ['name', ]
    list_filter = ['festival','visible'] 
    list_editable=['visible','email', 'country',  'homepage', ]
    inlines = [ArtInline] #PersonInline, , DocumentationInline]
    fieldsets = [
            (None, {'fields': ['visible', 'festival', 'event', 'name', 'slug', 'email',
    'country', 'phone', 'homepage', 'bio', 'statement']}),
           ('images', {'fields': ['headshot', 'poster']}),
           ('layout', {'fields': ['template', 'css', 'javascript'], 'classes': ['collapse']}),
            ]
admin.site.register(models.Artist, ArtistAdmin) 
    
