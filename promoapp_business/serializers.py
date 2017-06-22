from rest_framework import serializers

from .models import *

# *****************************************************************************
# **********************            VIEW            ***************************
# *****************************************************************************
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('pk', 'name', 'rif', 'commercial_sector', 'address', 'email')

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('pk', 'name', 'rif', 'address', 'email')

# *****************************************************************************
# **********************            CREATE           **************************
# *****************************************************************************
class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'rif', 'commercial_sector', 'address', 'email')

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'rif', 'address', 'email')

# *****************************************************************************
# **********************             EDIT            **************************
# *****************************************************************************
class CompanyEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'rif', 'commercial_sector', 'address', 'email')

class StoreEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'rif', 'address', 'email')