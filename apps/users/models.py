from django.db import models
from django.contrib.auth.models import AbstractUser


class EstoreUser(AbstractUser):
    """
        Django ni ozini User modelini ustidan
        yozvoryapmiz, bzda 3ta tipdagi foy-chi
        boladi: Admin, Store Admin, Client
    """

    USER_TYPE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STORE_ADMIN', 'Store Admin'),
        ('CLIENT', 'Client')
    )

    user_type = models.CharField(max_length=20,
            choices=USER_TYPE_CHOICES,
            default='CLIENT')
    
    phone_number = models.CharField(max_length=15,
            blank=True,
            null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
    
    def __str__(self):
        return self.get_full_name()
