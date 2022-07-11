from django.db.models.signals import pre_save
from collector.models.pathfinder_weapon import PathfinderWeapon
from django.dispatch import receiver


@receiver(pre_save, sender=PathfinderWeapon, dispatch_uid='update_weapon')
def update_weapon(sender, instance, conf=None, **kwargs):
    instance.is_weapon = True
