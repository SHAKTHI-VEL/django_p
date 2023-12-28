from rest_framework import serializers
from .models import Team

class team_serializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'
