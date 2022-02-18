from django.db import models



class Actor(models.Model):
    G=(
        ("erkak","erkak"),
        ("ayol","ayol"),
    )
    name=models.CharField(max_length=30)
    birth_date=models.DateField()
    gender=models.CharField(max_length=10,choices=G)
    def __str__(self):
        return self.name
class Movie(models.Model):
    J=(
        ("action","action"),
        ("drama","drama"),
        ("comedy","comedy"),
    )
    title=models.CharField(max_length=50)
    janr=models.CharField(max_length=12,choices=J)
    date=models.DateField()
    actor=models.ManyToManyField(Actor)
    def __str__(self):
        return self.title
class Comment(models.Model):
    matn=models.TextField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    def __str__(self):
        return self.matn




