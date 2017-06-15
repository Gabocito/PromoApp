from rest_framework import serializers

from .models import *

# *****************************************************************************
# **********************            VIEW            ***************************
# *****************************************************************************
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('description', 'products', 'discount')

class AdvertisingCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisingCampaign
        fields = ('target', 'start_date', 'end_date')

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'rif', 'address', 'email')

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('name', 'rif', 'address', 'email')

# *****************************************************************************
# **********************            CREATE           **************************
# *****************************************************************************
class PromotionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('description', 'products', 'discount')

class AdvertisingCampaignCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisingCampaign
        fields = ('target', 'start_date', 'end_date')

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'rif', 'address', 'email')

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'rif', 'address', 'email')