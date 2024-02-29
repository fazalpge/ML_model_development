from rest_framework import serializers
from myapi.models import Attritiondata

class serializerclass(serializers.ModelSerializer):
    class Meta:
        model = Attritiondata
        fields = '__all__'