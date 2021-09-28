from rest_framework.serializers import ModelSerializer
from api.models import Poverka


class PoverkiSerializer(ModelSerializer):
    class Meta:
        model = Poverka
        fields = '__all__'
