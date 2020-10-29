from rest_framework import serializers 
from .models import ProfileEvaluation

class Profile(serializers.ModelSerializer):
    class Meta:
        model = ProfileEvaluation
        fields = '__all__'

