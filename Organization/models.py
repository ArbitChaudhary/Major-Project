from django.db import models

# Create your models here.
class UserInfo(models.Model):
    Username= models.CharField(primary_key=True, max_length=14)
    First_name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Username}"


