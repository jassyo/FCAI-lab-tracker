from django.db import models

STAUTS_CHOICES =(
    ("working","operating"),
    ("not working","borken")
)
# Create your models here.
class Catalog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

class Users(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=80)
    jobTitle = models.CharField(max_length=80)
    userName = models.CharField(max_length=120)
    password = models.CharField(max_length=16)

class Labs(models.Model):
    labName = models.CharField(max_length=120)
    labBuilding = models.CharField(max_length=120)
    labFNumber = models.IntegerField()
    labPcsCount= models.PositiveIntegerField()
    labChairsCount = models.PositiveIntegerField()
    labStatus= models.CharField(
        max_length = 20,
        choices = STAUTS_CHOICES,
        default = 'working'
        )

class Pcs(models.Model):
    labId = models.IntegerField()
    pcStatus= models.CharField(
        max_length = 20,
        choices = STAUTS_CHOICES,
        default = 'working'
        )
    comment = models.TextField()

    def _str_(self):
        return self.title