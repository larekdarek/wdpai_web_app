from rest_framework import serializers
from .models import TeamMember

#Serializer dla aplikacji 'team', przekształca obiekt modeli na JSON i weryfikuje dane
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'first_name', 'last_name', 'role']
