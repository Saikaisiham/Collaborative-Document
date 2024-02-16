from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Notification
from base.models import UploadedDocument



@receiver(m2m_changed, sender=UploadedDocument.participants.through)
def notify_participant_added(sender, instance, action, **kwargs):
    if action == 'post_add':
        for user_id in kwargs['pk_set']:
            user = User.objects.get(pk=user_id)
            Notification.objects.create(user=user, message=f'You have been added to document {instance.id}')
