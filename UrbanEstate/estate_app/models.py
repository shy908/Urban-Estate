from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django import forms
from .models import UploadMedia


def media_upload_path(instance, filename):
    return f'media/{filename}'

class UploadMedia(models.Model):
    MEDIA_CHOICES = (
        ('video', 'Video'),
        ('image', 'Image'),
    )

    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    file = models.FileField(upload_to=media_upload_path)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default='file')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'estate_app_uploadmedia'

    def __str__(self):
        return self.title

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('subscriber', 'Subscriber'),
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set'
    )

    def __str__(self):
        return self.username

    class MyImageForm(forms.ModelForm):
        class Meta:
            model = UploadMedia
            fields = ('image',)
