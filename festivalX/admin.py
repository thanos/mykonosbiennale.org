from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import Participant, ParticipantRole, Curator, Organiser, Artist, Dancer, Director #, StandardModel




    
 



class ParticipantRoleChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = ParticipantRole

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
#     base_form = ...
#     base_fieldsets = (
#         ...
#     )


class ArtistAdmin(ParticipantRoleChildAdmin):
    base_model = Artist
    # define custom features here


class DirectorAdmin(ParticipantRoleChildAdmin):
    base_model = Director
    # define custom features here


class RoleParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = ParticipantRole
    child_models = (
        (Artist, ArtistAdmin),
        (Director, DirectorAdmin),
    )


class ParticipantRoleInline(admin.StackedInline):
    model = ParticipantRole
    #fk_name = 'modelb'
    #readonly_fields = ['modela_ptr']


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ParticipantRoleInline]


# Only the parent needs to be registered:
admin.site.register(ParticipantRole, RoleParentAdmin)
#admin.site.register(StandardModel, StandardModelAdmin)