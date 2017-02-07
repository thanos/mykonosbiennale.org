from django.contrib import admin
import models 
from django.http import HttpResponse

class FestivalAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', ]   
admin.site.register(models.Festival, FestivalAdmin)  

class ProjectAdmin(admin.ModelAdmin):   
    list_filter = ['festival',] 
    list_display = ['title', 'festival']   
admin.site.register(models.Project, ProjectAdmin)  


class ArtAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['artist', 'title',  'photo',  'description', 'text']   
    search_fields = ['title', 'description','text']
    list_filter = ['project'] 
admin.site.register(models.Art, ArtAdmin)        



 
class ArtInline(admin.TabularInline):
    model = models.Art
    extra = 3
    
class ArtistAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'festival','event', 'headshot', 'country','visible']
    search_fields = ['name', ]
    list_filter = ['festival', 'event', 'visible'] 
    list_editable=['visible','event', 'festival', 'country',  'headshot', ]
    inlines = [ArtInline] #PersonInline, , DocumentationInline]
    fieldsets = [
            (None, {'fields': ['visible', 'festival', 'event', 'name', 'slug', 'email',
    'country', 'phone', 'homepage', 'bio', 'statement']}),
           ('images', {'fields': ['headshot', 'poster']}),
           ('layout', {'fields': ['template', 'css', 'javascript'], 'classes': ['collapse']}),
            ]

    actions=['export_emails', 'export_names']
    def export_emails(self, request, queryset):
        emails = set()
        for film in queryset:
            emails.add(film.contact_email)
        text = ",".join(list(emails))
        return HttpResponse(text, content_type="text/plain")
    
    def export_names(self, request, queryset):
        names = set()
        for film in queryset.order_by('name'):
            names.add(film.name)
        text = ", ".join(sorted(names))
        return HttpResponse(text, content_type="text/plain")
    
admin.site.register(models.Artist, ArtistAdmin) 