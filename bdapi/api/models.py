from django.db import models

# Create your models here.

class Human(models.Model):

    GENDER = (
        ('male','male'),
        ('female','female'),
        ('other','other'),
    )

    CAT = (
        ('friends','friends'),
        ('family','family'),
    )

    id = models.AutoField(primary_key=True)
    human_name = models.CharField(max_length=100,blank=False,unique=True)
    human_dob = models.DateField(blank=False)
    human_gender = models.CharField(max_length=20,null=False,choices=GENDER)
    category = models.CharField(max_length=20,null=True,blank=False,choices=CAT)

    def __str__(self):
        return self.human_name

    
