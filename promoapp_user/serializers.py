from rest_framework import serializers

from django.contrib.auth.models import User as django_User

from .models import *

# *****************************************************************************
# **********************          DETAILS           ***************************
# *****************************************************************************
class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('username', 'first_name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = User
        fields = ('pk', 'user', 'acc_type', 'email')

class StoreManagerSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = StoreManager
        fields = ('pk', 'user', 'is_active', 'email')

class PromotionManagerSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = PromotionManager
        fields = ('pk', 'user', 'is_active', 'email')

class AdminSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = Admin
        fields = ('pk', 'user', 'email')

# *****************************************************************************
# **********************            CREATE           **************************
# *****************************************************************************
class DjangoUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('username', 'password')

class UserCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = User
        fields = ('user', 'email')

class StoreManagerCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = StoreManager
        fields = ('user', 'email')

class PromotionManagerCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = PromotionManager
        fields = ('user', 'email')

class AdminCreateSerializer(serializers.ModelSerializer):
    user = DjangoUserCreateSerializer()

    class Meta:
        model = Admin
        fields = ('user', 'email')

# *****************************************************************************
# **********************             EDIT            **************************
# *****************************************************************************
class DjangoUserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = django_User
        fields = ('first_name', 'last_name', 'password')

class UserEditSerializer(serializers.ModelSerializer):
    user = DjangoUserEditSerializer()

    class Meta:
        model = User
        fields = ('user',)

class StoreManagerEditSerializer(serializers.ModelSerializer):
    user = DjangoUserEditSerializer()

    class Meta:
        model = StoreManager
        fields = ('user', )

class PromotionManagerEditSerializer(serializers.ModelSerializer):
    user = DjangoUserEditSerializer()

    class Meta:
        model = PromotionManager
        fields = ('user',)

class AdminEditSerializer(serializers.ModelSerializer):
    user = DjangoUserEditSerializer()

    class Meta:
        model = Admin
        fields = ('user',)