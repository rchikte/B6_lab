from audioop import maxpp
from tkinter import Y
from django.db import models

# Create your models here.

class ActiveBookManager(models.Manager):    # custom model manager
    def get_queryset(self):
        return super(ActiveBookManager, self).get_queryset().filter(is_active="Y")

class InActiveBookManager(models.Manager):  # custom model manager
    def get_queryset(self):
        return super(InActiveBookManager, self).get_queryset().filter(is_active="N")

class Book(models.Model):
    name =models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.CharField(max_length=1, default= "Y")
    active_objects = ActiveBookManager()
    inactive_objects = InActiveBookManager()
    objects = models.Manager()

    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.name}"



    

