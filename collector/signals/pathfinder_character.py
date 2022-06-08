from django.db.models.signals import pre_save
from collector.models.pathfinder_character import PathfinderCharacter
from django.dispatch import receiver


@receiver(pre_save, sender=PathfinderCharacter, dispatch_uid='update_character')
def update_character(sender, instance, conf=None, **kwargs):
    instance.fix()
