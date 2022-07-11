from django.contrib import admin
from collector.models.pathfinder_character import PathfinderCharacter, PathfinderCharacterAdmin
from collector.models.pathfinder_race import PathfinderRace, PathfinderRaceAdmin
from collector.models.pathfinder_level import PathfinderLevel, PathfinderLevelAdmin
from collector.models.pathfinder_class import PathfinderClass, PathfinderClassAdmin
from collector.models.pathfinder_skill import PathfinderSkill, PathfinderSkillAdmin
from collector.models.pathfinder_feat import PathfinderFeat, PathfinderFeatAdmin
from collector.models.pathfinder_gear import PathfinderGear, PathfinderGearAdmin
from collector.models.pathfinder_weapon import PathfinderWeapon, PathfinderWeaponAdmin
from collector.models.pathfinder_armor import PathfinderArmor, PathfinderArmorAdmin
from collector.models.pathfinder_rank import PathfinderRank, PathfinderRankAdmin
from collector.models.pathfinder_spell import PathfinderSpell, PathfinderSpellAdmin
from collector.models.pathfinder_equipment import PathfinderEquipment, PathfinderEquipmentAdmin
from collector.models.pathfinder_special_ability import PathfinderSpecialAbility, PathfinderSpecialAbilityAdmin

# Register your models here.
admin.site.register(PathfinderRace, PathfinderRaceAdmin)
admin.site.register(PathfinderCharacter, PathfinderCharacterAdmin)
admin.site.register(PathfinderLevel, PathfinderLevelAdmin)
admin.site.register(PathfinderClass, PathfinderClassAdmin)
admin.site.register(PathfinderSkill, PathfinderSkillAdmin)
admin.site.register(PathfinderRank, PathfinderRankAdmin)
admin.site.register(PathfinderFeat, PathfinderFeatAdmin)
admin.site.register(PathfinderGear, PathfinderGearAdmin)
admin.site.register(PathfinderWeapon, PathfinderWeaponAdmin)
admin.site.register(PathfinderArmor, PathfinderArmorAdmin)
admin.site.register(PathfinderSpell, PathfinderSpellAdmin)
admin.site.register(PathfinderEquipment, PathfinderEquipmentAdmin)
admin.site.register(PathfinderSpecialAbility, PathfinderSpecialAbilityAdmin)
