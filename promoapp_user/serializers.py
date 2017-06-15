from rest_framework import serializers

from .models import *

from django.contrib.auth.models import User as django_User

# *****************************************************************************
# **********************            LOGIN            **************************
# *****************************************************************************
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('username', 'password')

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
        fields = ('user', 'user_type', 'acc_type')

class StoreManagerSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = StoreManager
        fields = ('user', 'acc_type')

class PromotionManagerSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = PromotionManager
        fields = ('user', 'acc_type')

class AdminSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = Admin
        fields = ('user', 'user_type')

# *****************************************************************************
# **********************            CREATE           **************************
# *****************************************************************************
class DjangoUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('first_name', 'password', 'email')

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
