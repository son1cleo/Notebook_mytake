from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NoteBooks(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now = True)
    title = models.CharField(max_length=100,null=False,blank=False,default = "Default")
    description = models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    class Meta:
        verbose_name = "User Notes"

    def __str__(self):
        return self.title
        

