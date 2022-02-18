from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Actor,Movie,Comment

class ActorSerializer(ModelSerializer):
    class Meta:
        model=Actor
        fields=["name","birth_date","gender"]

class MovieSerializer(ModelSerializer):

    class Meta:
        model=Movie
        fields=["id","title","janr","date","actor"]
    def validate_title(self,qiymat):
        if len(qiymat)<=3:
            raise ValidationError(detail="Bunaqa aktyor yoq")
        return qiymat

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        field=["id","matn","movie"]
