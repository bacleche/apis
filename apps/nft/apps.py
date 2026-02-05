from django.apps import AppConfig

class NftConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.nft"

    def ready(self):
        import apps.nft.signals  # Import obligatoire pour activer les signals
