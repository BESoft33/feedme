from django.db import models
from django.db.models import Q
from uuid import uuid4
from django.conf import settings

UserModel = settings.AUTH_USER_MODEL

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    name = models.CharField(max_length=200)    
    manager = models.ForeignKey(UserModel, 
                                on_delete=models.CASCADE, 
                                related_name='restaurant', 
                                related_query_name='manager',limit_choices_to=Q(role = 1))
    

class RestaurantDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    restaruant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='details', related_query_name='restaurant')
    location = models.CharField(max_length=200)
    open_at = models.TimeField()
    close_at = models.TimeField()


    # @property
    # def is_open(self):
    #     from datetime import datetime
    #     now  = datetime.datetime.now().time()
    #     return self.open_at < now < self.close_at





