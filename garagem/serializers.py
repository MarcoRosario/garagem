from rest_framework.serializers import ModelSerializer

from garagem.models import Marca

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"