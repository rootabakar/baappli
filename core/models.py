from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


TYPE = (
    ("MALE", "MALE"),
    ("FEMELLE", "FEMELLE")
)

CATEGORIE = (
    ("CHIEN", "CHIEN"),
    ("CHAT", "CHAT")
)


class AjoutAnimal(models.Model):
    nom = models.CharField(max_length=125)
    age = models.IntegerField()
    image = models.ImageField(upload_to='Images')
    type = models.CharField(max_length=125, choices=TYPE)
    categorie = models.CharField(max_length=100, choices=CATEGORIE)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(AjoutAnimal, on_delete=models.CASCADE)

