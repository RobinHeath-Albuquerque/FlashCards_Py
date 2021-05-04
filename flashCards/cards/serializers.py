from rest_framework import serializers
from .models import FlashCards, Collection


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCards
        fields = ['code', 'definition']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title']