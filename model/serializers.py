from rest_framework import serializers
from model.models import Data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Data
        fields = ['id','employee_name','dob','state','pincode','salary','joining_month','joining_year']
