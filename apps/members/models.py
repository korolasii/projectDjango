from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class UserProfile(AbstractUser):
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True)
    address = models.CharField(verbose_name='Адреса', max_length=255, blank=True, null=True)
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='users',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
        )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70}
    )
    
    groups = models.ManyToManyField(
        Group,
        verbose_name='Groups',
        related_name='user_profiles_groups',  # Задайте другое имя
        related_query_name='user_profile_group'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='User Permissions',
        related_name='user_profiles_permissions',  # Задайте другое имя
        related_query_name='user_profile_permission'
    )
    