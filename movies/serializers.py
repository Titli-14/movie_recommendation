from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=100)
    rating = serializers.FloatField()
    release_date = serializers.DateField()

class ReviewSerializer(serializers.Serializer):
    movie_id = serializers.CharField(max_length=255)
    user = serializers.CharField(max_length=255)
    review_text = serializers.CharField()
    rating = serializers.FloatField()