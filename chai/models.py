from django.db import models
from django.utils import timezone #In utils timezon and some other functions aare present
# Create your models here.


class ChaiVarity(models.Model):
    #creating enum to restrict user
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('EL','ELAICHI'),
    ]
    name=models.CharField(max_length=100)
    # We can not use ImageField with out having Pillow
    image=models.ImageField(upload_to=("chais/"))
    date_added=models.DateTimeField(default=(timezone.now))
    type=models.CharField(max_length=2,choices= CHAI_TYPE_CHOICE)
    description=models.TextField(default='')

    # Modifying the admin panel
    def __str__(self):
        return self.name
    
    

