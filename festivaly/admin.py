from django.contrib import admin

from . import models 



admin.site.register(models.Media) 
admin.site.register(models.Album)
admin.site.register(models.Festival)
admin.site.register(models.Project)
admin.site.register(models.FestivalProject)

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['festival_project','participant',  'headshot_tag']
admin.site.register(models.Participation, ParticipationAdmin)

admin.site.register(models.Art)

class ParticipantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name',  'headshot_tag']
admin.site.register(models.Participant, ParticipantAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['festival_project','participant',  'headshot_tag', 'art']
    
admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.FilmDirector)
admin.site.register(models.Film)
admin.site.register(models.Organizer)

    