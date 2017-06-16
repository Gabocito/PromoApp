from rest_framework import serializers

from .models import *

from django.contrib.auth.models import User as django_User

# *****************************************************************************
# **********************          DETAILS           ***************************
# *****************************************************************************
class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = User
        fields = ('user', 'acc_type', 'pk')

class StoreManagerSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = StoreManager
        fields = ('user', 'is_active', 'pk')

class PromotionManagerSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = PromotionManager
        fields = ('user', 'is_active', 'pk')

class AdminSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = Admin
        fields = ('user', 'pk')

# *****************************************************************************
# **********************            CREATE           **************************
# *****************************************************************************
class DjangoUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('username', 'email', 'password')

class UserCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = User
        fields = ('user', 'acc_type')

class StoreManagerCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = StoreManager
        fields = ('user', 'is_active')

class PromotionManagerCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = PromotionManager
        fields = ('user', 'is_active')

class AdminCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = Admin
        fields = ('user',)