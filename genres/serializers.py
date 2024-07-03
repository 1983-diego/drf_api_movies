from rest_framework import serializers
from genres.models import Genre

# serializers: tratam os dados que vem do banco de dados para serem entregues no formato
# json para o front-end.

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
