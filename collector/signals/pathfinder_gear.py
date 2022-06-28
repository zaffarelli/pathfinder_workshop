from django.db.models.signals import pre_save
from collector.models.pathfinder_gear import PathfinderGear
from django.dispatch import receiver


@receiver(pre_save, sender=PathfinderGear, dispatch_uid='update_gear')
def update_gear(sender, instance, conf=None, **kwargs):
    instance.fix()
