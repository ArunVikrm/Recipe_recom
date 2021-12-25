from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Recipe,Image

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']