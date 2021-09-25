from django.db import models
from django.db.models.fields import BooleanField
from accounts.models import CustomUser as User
from components.models import Component

# Create your models here.

class Bag(models.Model):
    bag_id = models.CharField(max_length = 50, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Bag'
        verbose_name_plural = 'Bag Details'

    def __str__(self):
        return str(self.bag_id)
    

class BagItem(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    component = models.ForeignKey(Component, on_delete = models.CASCADE)
    bag = models.ForeignKey(Bag, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Bag Item'
        verbose_name_plural = 'Bag Items'

    def __str__(self):
        return str(self.component.name)
        
