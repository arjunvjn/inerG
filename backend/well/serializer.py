from rest_framework import serializers
from .models import Ohio

class OhiolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ohio
        exclude = ('api_well_number', 'quater','id')