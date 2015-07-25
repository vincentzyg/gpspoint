from django.db import models

# Create your models here.
class Userdata(models.Model):
    user_id=models.IntegerField()
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)    
    age = models.IntegerField()
    blood_type=models.CharField(max_length=6)
    emergency_number = models.IntegerField()
    destination=models.CharField(max_length=20)
    
    class Meta:
        unique_together = (("user_id", "username"),)

    def __unicode__(self):
        return self.username

class Sensordata(models.Model):
    user=models.ForeignKey('Userdata')#Userdata's Primary Key
    timestamp=models.DateTimeField()
    lan=models.FloatField(null=True)
    lon=models.FloatField(null=True)
    

#    def __unicode__(self):
#        return self.timestamp

