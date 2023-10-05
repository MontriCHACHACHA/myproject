from myapp.models import product,datauser
from rest_framework import serializers

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = product
        fields = ['id','url', 'name', 'price']

class DatauserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = datauser
        fields = ['id','url', 'fname', 'lname', 'address', 'phone']