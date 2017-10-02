from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect

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

admin.site.register(models.Location)

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
    list_display = ['id','ref',  'title', 'projection_copy', 'projection_copy_url', 'dir_by' , 'trailer_url', 'trailer_embed', 'film_type', 'project',  'status', 'film_type', 'present','when',   ] #, 'length']
    search_fields = ['ref','title',  'dir_by', 'synopsis',  ]
    list_editable=['status', 'project', 'trailer_url', 'trailer_embed', 'projection_copy', 'projection_copy_url', 'present','when' ]
    list_filter = [ 'status','film_type', 'source','projection_copy', 'present', 'project']
    inlines = [ImageInline,] #PersonInline, , DocumentationInline]
    actions=['export_emails', 'export_posts', 'export_directors', 'export_titles','send_emails']
    def export_emails(self, request, queryset):
        emails = set()
        for film in queryset:
            emails.add(film.contact_email)
        text = ",".join(list(emails))
        return HttpResponse(text, content_type="text/plain")
    
    def export_directors(self, request, queryset):
        dir_by = set()
        for film in queryset.order_by('dir_by'):
            dir_by.add(film.dir_by)
        text = ", ".join(list(dir_by))
        return HttpResponse(text, content_type="text/plain")
    
    def export_titles(self, request, queryset):
        dir_by = set()
        for film in queryset.order_by('dir_by'):
            dir_by.add(film.title)
        text = ", ".join(list(dir_by))
        return HttpResponse(text, content_type="text/plain")    
    
    def export_posts(self, request, queryset):
        dir_by = set()
        for film in queryset.order_by('dir_by'):
            dir_by.add("Showing 7th July at the Laka Theatre\n\n{}".format(film.absolute_url))
        text = "\n\n".join(list(dir_by))
        return HttpResponse(text, content_type="text/plain")    
        
    def send_emails(self, request, queryset):
        selected = ','.join([str(film.pk) for film in queryset.order_by('title')])
        return HttpResponseRedirect("/filmfestival/send_emails/?&ids=%s" % selected)
    
admin.site.register(models.Film, FilmAdmin) 

    
class RewardInline(admin.TabularInline):
    model = models.Reward
    extra = 0

admin.site.register(models.Reward) 
admin.site.register(models.Award) 
    
class DayInline(admin.TabularInline):
    model = models.Day
    extra = 0
    
class ScreeningInline(admin.TabularInline):
    model = models.Screening
    extra = 1
    exclude = ('slug',)
    fields = ('pause', 'start_time',  'film', )
    
    
class ProgramAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title'] 
    inlines = [DayInline] 
admin.site.register(models.Program, ProgramAdmin) 

class DayAdmin(admin.ModelAdmin):
    save_on_top  = True
    list_display = ['program', 'date', 'number_of_films',  'runtime'] 
    list_filter = [ 'program']
    exclude = ('slug',)
    inlines = [ScreeningInline] 
    def build_timetable(self, request, queryset):
        for day in queryset:            
            day.build_timetable()
    build_timetable.short_description = "Recalulate all the timetables"   
    actions=[build_timetable]
admin.site.register(models.Day, DayAdmin) 



class ScreeningAdmin(admin.ModelAdmin):
    save_on_top  = True
    list_display = ['day', 'pause', 'start_time',  'film',] 
    list_filter = [ 'day']
    exclude = ('slug',)
    search_fields = ['film__title',  'film__dir_by']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "film":      
            print "FILM"
            kwargs["queryset"] = models.Film.objects.filter(status=models.Film.SELECTED).exclude(film_type = models.Film.VIDEO_GRAFITTI).order_by('title')
        return super(ScreeningAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
   
admin.site.register(models.Screening, ScreeningAdmin) 
