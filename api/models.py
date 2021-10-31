from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} {self.lastname}"
