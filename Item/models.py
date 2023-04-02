from django.db import models
import uuid
# Create your models here.

class FOODITEM(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to='Item/foodpicture',null=True,blank=True)
    cooking_time=models.PositiveIntegerField()
    category=models.ManyToManyField('CATEGORY',blank=True) 
    
    def __str__(self):
        return self.name
    

class CATEGORY(models.Model):
    name= models.CharField(max_length=200)
    created  = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='Item/foodpicture',null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.name