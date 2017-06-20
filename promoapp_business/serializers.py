from rest_framework import serializers

from .models import *

# *****************************************************************************
# **********************            VIEW            ***************************
# *****************************************************************************
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('pk', 'description', 'products', 'discount')

class AdvertisingCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisingCampaign
        fields = ('pk', 'target', 'start_date', 'end_date')

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
        fields = ('name', 'rif', 'commercial_sector', 'address', 'email')

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'rif', 'address', 'email')

# *****************************************************************************
# **********************             EDIT            **************************
# *****************************************************************************
class PromotionEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('description', 'products', 'discount')

class AdvertisingCampaignEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisingCampaign
        fields = ('target', 'start_date', 'end_date')

class CompanyEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'rif', 'commercial_sector', 'address', 'email')

class StoreEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'rif', 'address', 'email')