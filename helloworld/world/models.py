from django.db import models
class World(models.Model):
    title = models.CharField(max_length=20)

    contet = models.TextField()

    user = models.CharField(max_length=30)
# Create your models here.
#self는 자기자신을 의미함
    def __str__(self):
        return self.title

# Create your models here.
