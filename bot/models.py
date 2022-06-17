from django.db import models

# Create your models here.
from django.db import models

# baza


class Profile(models.Model):
    exeterenal_id=models.PositiveIntegerField(
        verbose_name="user id",
        null=False
    )
    username=models.TextField(
        verbose_name="username",
        null=True,
        blank=True
    )
    f_name=models.TextField(
        verbose_name="First_name",
    )
    l_name=models.TextField(
        verbose_name="Lastname",
        null=True
    )


    def __str__(self):
        return  f'#{self.exeterenal_id}  { self.f_name}'



    class Meta:
        verbose_name="Profili"