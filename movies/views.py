from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mongo_utils import movies_collection, reviews_collection
from .serializers import MovieSerializer, ReviewSerializer
from bson import ObjectId  # For handling MongoDB ObjectId

# Get all movies
@api_view(['GET'])
def get_movies(request):
    movies = list(movies_collection.find())
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# Add a new movie
@api_view(['POST'])
def add_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        movie_data = serializer.validated_data
        movies_collection.insert_one(movie_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Search movies by title, genre, or rating
@api_view(['GET'])
def search_movies(request):
    query = request.GET.get('query', '')
    movies = list(movies_collection.find({
        "$or": [
            {"title": {"$regex": query, "$options": "i"}},  # Case-insensitive search
            {"genre": {"$regex": query, "$options": "i"}},
            {"rating": {"$gte": float(query) if query.replace('.', '', 1).isdigit() else 0}}
        ]
    }))
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# Get movie recommendations based on genre or rating
@api_view(['GET'])
def recommend_movies(request):
    genre = request.GET.get('genre', '')
    min_rating = float(request.GET.get('min_rating', 0))
    movies = list(movies_collection.find({
        "genre": {"$regex": genre, "$options": "i"},  # Case-insensitive genre search
        "rating": {"$gte": min_rating}  # Minimum rating filter
    }))
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# Add a review for a movie
@api_view(['POST'])
def add_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review_data = serializer.validated_data
        reviews_collection.insert_one(review_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get reviews for a specific movie
@api_view(['GET'])
def get_reviews(request, movie_id):
    reviews = list(reviews_collection.find({"movie_id": movie_id}))
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)