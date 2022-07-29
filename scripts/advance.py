from collector.models.pathfinder_advancement import PathfinderClassAdvancement
from collector.models.pathfinder_class import PathfinderClass

for c in PathfinderClass.objects.all():
    for l in range(20):
        all_adv = PathfinderClassAdvancement.objects.filter(pathfinder_class=c, level=l+1)
        if not len(all_adv):
            a = PathfinderClassAdvancement()
            a.pathfinder_class = c
            a.level = l+1
            a.save()
            print(f'Added... {a}')



