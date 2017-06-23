from rest_framework import serializers

from .models import *

# *****************************************************************************
# **********************            VIEW            ***************************
# *****************************************************************************
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('pk', 'description', 'products', 'discount', 'is_active')

class AdvertisingCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisingCampaign
        fields = ('pk', 'target', 'start_date', 'end_date', 'is_active')

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