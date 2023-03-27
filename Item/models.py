from django.db import models
import uuid
# Create your models here.

class FOODITEM(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to='Item/foodpicture',null=True,blank=True)
    cooking_time=models.PositiveIntegerField()
    category=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name