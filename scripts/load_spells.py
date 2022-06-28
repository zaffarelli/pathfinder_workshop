from collector.models.pathfinder_spell import PathfinderSpell
from collector.utils.spells_import import get_spells



# Clean up
es = PathfinderSpell.objects.all()
for e in es:
    e.delete()

get_spells()
