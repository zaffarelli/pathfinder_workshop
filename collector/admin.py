from django.contrib import admin
from collector.models.pathfinder_character import PathfinderCharacter, PathfinderCharacterAdmin
from collector.models.pathfinder_race import PathfinderRace, PathfinderRaceAdmin
from collector.models.pathfinder_class_level import PathfinderClassLevel, PathfinderClassLevelAdmin
from collector.models.pathfinder_class import PathfinderClass, PathfinderClassAdmin

# Register your models here.
admin.site.register(PathfinderRace, PathfinderRaceAdmin)
admin.site.register(PathfinderCharacter, PathfinderCharacterAdmin)
admin.site.register(PathfinderClassLevel, PathfinderClassLevelAdmin)
admin.site.register(PathfinderClass, PathfinderClassAdmin)
