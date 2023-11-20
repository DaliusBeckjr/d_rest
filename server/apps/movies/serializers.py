from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'duration']

    def create(self, validated_data):
        movie_instance = super().create(validated_data)
        self.print_movie_info(movie_instance)
        return movie_instance

    def print_movie_info(self, movie_instance):
        print(f"""Title: {movie_instance.title}
                Description: {movie_instance.description}
                Release Date: {movie_instance.release_date}
                Duration: {movie_instance.duration}""")