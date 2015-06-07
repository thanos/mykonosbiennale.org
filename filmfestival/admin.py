from django.contrib import admin
import models 

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email'] 
    search_fields = ['name', 'email', 'info']
    
admin.site.register(models.Person, PersonAdmin)    

class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'image_type', 'image']   
    search_fields = ['title', 'info']
      
admin.site.register(models.Image, ImageAdmin)  



class DocumentationAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', ]   

      
admin.site.register(models.Documentation, DocumentationAdmin)  


class PersonInline(admin.TabularInline):
    model = models.Person
    extra = 3
    

    
class ImageInline(admin.TabularInline):
    prepopulated_fields = {"slug": ("title",)}
    model = models.Image
    extra =6
 
class DocumentationInline(admin.TabularInline):
    model = models.Documentation
    extra = 3
    
class FilmAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['ref', 'status', 'film_type', 'title', 'dir_by'] #, 'length']
    search_fields = ['title', 'dir_by', 'synopsis' ]
    list_editable=['status', 'film_type', ]
    list_filter = [ 'status','film_type','source'] 
    inlines = [ImageInline] #PersonInline, , DocumentationInline]
admin.site.register(models.Film, FilmAdmin) 
    
    

    
