from django.contrib import admin
from django.http import HttpResponse

import models


class FestivalAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', ]   
admin.site.register(models.Festival, FestivalAdmin)  

class ProjectAdmin(admin.ModelAdmin):   
    list_filter = ['festival',] 
    list_display = ['title', 'festival' ,'slug']   
admin.site.register(models.Project, ProjectAdmin)  


class ProjectXAdmin(admin.ModelAdmin):
    #list_filter = ['festival',]
    list_display = ['title','slug']
admin.site.register(models.ProjectX, ProjectXAdmin)

admin.site.register(models.ProjectSeason) 

class ArtAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['pk', 'artist', 'title',  'project_x', 'project', 'leader', 'image_tag', 'show', 'photo',  'description', 'text']
    search_fields = ['title', 'description','text']
    list_filter = ['project', 'leader','show'] 
    list_editable=['show', 'leader',  ]
    readonly_fields = ('image_tag',)
admin.site.register(models.Art, ArtAdmin)        



 
class ArtInline(admin.TabularInline):
    model = models.Art
    extra = 3
    
class ArtistAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['id', 'last_festival', 'name', 'email', 'event', 'headshot', 'country','visible']
    #list_display = ['name', 'festival','event', 'headshot', 'country','visible']
    search_fields = ['name', ]
    list_filter = ['event', 'visible'] 
    list_editable=['visible', 'last_festival', 'email', 'event',  'country',  'headshot', ]
    inlines = [ArtInline] #PersonInline, , DocumentationInline]
    fieldsets = [
            (None, {'fields': ['visible',  'event', 'name', 'slug', 'email',
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