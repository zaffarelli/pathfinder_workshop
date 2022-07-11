from django.apps import AppConfig


class CollectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collector'

    def ready(self):
        import collector.signals.pathfinder_character
        import collector.signals.pathfinder_gear
        import collector.signals.pathfinder_armor
        import collector.signals.pathfinder_weapon
