from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True) 
    return Response(serializer.data)


@api_view(['POST'])
def addMovie(request):
    data = request.data
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        movie_instance = serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


