from django.db.models.signals import pre_save
from collector.models.pathfinder_level import PathfinderLevel
from django.dispatch import receiver


@receiver(pre_save, sender=PathfinderLevel, dispatch_uid='update_level')
def update_level(sender, instance, conf=None, **kwargs):
    instance.fix()
