from django.conf.urls import url, include
from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets

from core.models import Review, Place, Category
from authentication.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'longitude', 'latitude', 'address')

class ReviewSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(many=False, write_only=True)
    categories = CategorySerializer(many=True)
    created_by = UserSerializer(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'short_description', 'information', 'place', 'categories', 'created_by')

    def create(self, validated_data):
        category_list=[]

        # create place manually (DRF doesn't handle nested creation or update)
        place_data = validated_data.pop('place')
        place, _ = Place.objects.get_or_create(**place_data)
        validated_data['place'] = place

        #we remove the category properties
        if 'categories' in validated_data:
            category_list = validated_data.pop('categories')

        #we create the review object
        review = Review.objects.create(**validated_data)

        #we add the category, one by one
        for category in category_list:
            newCategory, created = Category.objects.get_or_create(name=category['name'])
            review.categories.add(newCategory)

        return review

    def update(self, instance, validated_data):
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.information = validated_data.get('information', instance.information)

        # handle manually place
        place_data = validated_data.pop('place')
        place, _ = Place.objects.get_or_create(**place_data)
        instance.place = place

        instance.save()
        return instance

class PlacesSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ('name', 'longitude', 'latitude', 'address', 'reviews')
