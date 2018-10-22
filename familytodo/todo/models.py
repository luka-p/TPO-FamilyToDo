from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    nujnost = models.CharField(max_length=1, default='2')
    ime_otroka = models.CharField(max_length=10, default='')
    #family_kid = models.CharField(max_length=10)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Family(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def get_pass(self):
        return self.password

    def __str__(self):
        return self.name

class Kids(models.Model):
    family = models.CharField(max_length=10)
    kidname = models.CharField(max_length=10)

    def __str__(self):
        return self.kidname
