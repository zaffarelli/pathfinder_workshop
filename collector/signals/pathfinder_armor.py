from django.db.models.signals import pre_save
from collector.models.pathfinder_armor import PathfinderArmor
from django.dispatch import receiver


@receiver(pre_save, sender=PathfinderArmor, dispatch_uid='update_armor')
def update_armor(sender, instance, conf=None, **kwargs):
    instance.is_armor = True
