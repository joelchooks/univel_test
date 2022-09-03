from django.db.models.signals import post_save
from django.dispatch import receiver
from main_app.models import Post, PostDump

@receiver(post_save, sender=Post)
def update_after_post_is_saved(sender, instance: Post, created, **kwargs):
    if created:
        PostDump.objects.create(
            content = instance.__dict__
        )