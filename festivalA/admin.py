from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import Participant, Participation, Curator, Organiser, Artist, Dancer, Director, Art, Film,Tag #, StandardModel
import tagulous


import models


    
 



class ParticipationChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Participation

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
#     base_form = ...
#     base_fieldsets = (
#         ...
#     )


class DirectorshipInline(admin.TabularInline):
    model = Film.directed_by.through

class ArtAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['artist_name', 'title',   'description', 'tags',]   
    search_fields = ['artist_name', 'title', 'description',]
    #list_editable=['tags']
    list_filter = ('events','tags')
tagulous.admin.register(Art, ArtAdmin)        
tagulous.admin.register(Tag)

class FilmAdmin(admin.ModelAdmin):   
    prepopulated_fields = {"slug": ("title",)}
    list_display = [ 'title',  'synopsis', ]   
    search_fields = [ 'title', 'synopsis',]
    list_filter = ('directed_by',)
    exclude = ('directed_by',)
    inlines = [DirectorshipInline]
admin.site.register(Film, FilmAdmin)        

 
class ArtInline(admin.TabularInline):
    model = Art
    extra = 3
    
class FilmInline(admin.TabularInline):
    model = Film
    extra = 3    
    


class ArtistAdmin(ParticipationChildAdmin):
    base_model = Artist
    inlines = [ArtInline]
    # define custom features here


class DirectorAdmin(ParticipationChildAdmin):
    base_model = Director
    # define custom features here
    inlines = [DirectorshipInline]

class ParticipationParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Participation
    child_models = (
        (Artist, ArtistAdmin),
        (Director, DirectorAdmin),
    )


class ParticipationInline(admin.StackedInline):
    model = Participation
    fk_name = 'participant'
    #readonly_fields = ['participant_ptr']


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ParticipationInline]
    save_on_top  = True
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'tags']
    search_fields = ['name', ]
    #list_editable=['tags']


# Only the parent needs to be registered:
admin.site.register(Participation, ParticipationParentAdmin)
tagulous.admin.register(Participant, ParticipantAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Director, DirectorAdmin)



    
class EventAdmin(admin.ModelAdmin):
    #inlines = [ArtInline]
    save_on_top  = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['project', 'location', 'title', 'slug', ]
    search_fields = ['title', ]
admin.site.register(models.Event, EventAdmin)

class ProjectAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['festival', 'title', 'slug', ]
    search_fields = ['title', ]
admin.site.register(models.Project, ProjectAdmin)

class LocationAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'address', 'slug', ]
    search_fields = ['title', 'address']
admin.site.register(models.Location, LocationAdmin)

class FestivalAdmin(admin.ModelAdmin):
    save_on_top  = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['year', 'title',  'slug', ]
    search_fields = ['title',]
admin.site.register(models.Festival, FestivalAdmin)


