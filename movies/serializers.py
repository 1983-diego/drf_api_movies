from rest_framework import serializers
from movies.models  import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))
        if rate:
            return round(rate['stars__avg'], 1)
        return None
