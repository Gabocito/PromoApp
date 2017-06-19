from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from serializers import *

from models import *

from forms import *

from django.contrib.auth.models import User as django_User
from django.shortcuts import get_object_or_404
from django.db.models import Max
from django.http import Http404

# *****************************************************************************
# **********************            INDEX            **************************
# *****************************************************************************
class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/index.html'

    def get(self, request):        
        return Response({'index': 'It Works!'})

# *****************************************************************************
# **********************         CREATE/LIST        ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                               User                                    """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/user/users.html'

    """ List all users """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data

        users = django_User.objects.all()
        mx = users.aggregate(Max('id'))
        username = data['user']['email'] if data['user']['email'] != '' else data['user']['first_name'].lower() + str(mx)

        try:
            u = django_User.objects.create(username=data['user']['username']) 
        except:
            return Response({'error': 'User already exists!'}, 
                            status=status.HTTP_400_BAD_REQUEST)  
        u.set_password(data['user']['password']) 
        u.save()

        c = User.objects.create(user=u, acc_type=data['acc_type'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                          Store Manager                                """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StoreManagerFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/storemanager/form.html'

    def get(self, request, format=None):
        form = StoreManagerForm()
        return Response({'form': form})

class StoreManagerListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/storemanager/storemanagers.html'
    
    """ List all store managers """
    def get(self, request, format=None):
        storemanagers = StoreManager.objects.all()
        serializer = StoreManagerSerializer(storemanagers, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        form = StoreManagerForm(request.POST)
        if form.is_valid():
            data = {
                'user': {
                    'username': form.cleaned_data['username'],
                    'email': form.cleaned_data['email'],
                    'password': form.cleaned_data['password']
                },
                'is_active': True
            }
            serializer = StoreManagerCreateSerializer(data=data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data 
        try:
            u = django_User.objects.create(username=data['user']['username']) 
        except:
            return Response({'error': 'User already exists!'}, 
                            status=status.HTTP_400_BAD_REQUEST)  
        u.set_password(data['user']['password'])
        u.email = data['user']['email']
        u.save()

        s = StoreManager.objects.create(user=u, is_active=data['is_active'])

        storemanagers = StoreManager.objects.all()
        serializer = StoreManagerSerializer(storemanagers, many=True)
        
        return Response({'users': serializer.data}, status=status.HTTP_201_CREATED)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                         Promotion Manager                             """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionManagerFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/promotionmanager/form.html'

    def get(self, request, format=None):
        form = PromotionManagerForm()
        return Response({'form': form})

class PromotionManagerListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/promotionmanager/promotionmanagers.html'

    """ List all promotion managers """
    def get(self, request, format=None):
        promotionmanagers = PromotionManager.objects.all()
        serializer = PromotionManagerSerializer(promotionmanagers, many=True)
        return Response({'users': serializer.data})

    def post(self, request): 
        form = PromotionManagerForm(request.POST)
        if form.is_valid():
            data = {
                'user': {
                    'username': form.cleaned_data['username'],
                    'email': form.cleaned_data['email'],
                    'password': form.cleaned_data['password']
                },
                'is_active': True
            }
            serializer = PromotionManagerCreateSerializer(data=data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        try:
            u = django_User.objects.create(username=data['user']['username']) 
        except:
            return Response({'error': 'User already exists!'}, 
                            status=status.HTTP_400_BAD_REQUEST) 
        u.set_password(data['user']['password'])
        u.email = data['user']['email']
        u.save()

        s = PromotionManager.objects.create(user=u, is_active=data['is_active'])

        promotionmanagers = PromotionManager.objects.all()
        serializer = PromotionManagerSerializer(promotionmanagers, many=True)

        return Response({'users': serializer.data}, status=status.HTTP_201_CREATED)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                             Admin                                     """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class AdminListCreate(APIView):
    """ List all admins """
    def get(self, request, format=None):
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response({'users': serializer.data})

# *****************************************************************************
# **********************    DETAILS/UPDATE/DELETE   ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                               User                                    """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/user/user.html'

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        acc = {
            'FB': 'Facebook',
            'G': 'Google',
            'TW': 'Twitter'
        }
        data = {
            'username': serializer.data['user']['username'],
            'email': serializer.data['user']['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'acc_type': acc[serializer.data['acc_type']]
        }
        return Response({'user': data})

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                          Store Manager                                """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StoreManagerFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/storemanager/edit.html'

    def get_object(self, pk):
        try:
            return StoreManager.objects.get(pk=pk)
        except StoreManager.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        serializer = StoreManagerSerializer(storemanager)
        data = {
            'username': serializer.data['user']['username'],
            'email': serializer.data['user']['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Activo' if serializer.data['is_active'] else 'Inactivo',
            'pk': pk
        }
        form = StoreManagerEditForm()
        return Response({'form': form, 'user': data})

class StoreManagerView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/storemanager/storemanager.html'

    def get_object(self, pk):
        try:
            return StoreManager.objects.get(pk=pk)
        except StoreManager.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        serializer = StoreManagerSerializer(storemanager)
        data = {
            'username': serializer.data['user']['username'],
            'email': serializer.data['user']['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Activo' if serializer.data['is_active'] else 'Inactivo'
        }
        return Response({'user': data})

    def post(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        form = StoreManagerEditForm(request.POST)
        if form.is_valid():
            data = {
                'user': {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'password': form.cleaned_data['password']
                }
            }
            serializer = StoreManagerEditSerializer(data=data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        storemanager.user.set_password(data['user']['password'])
        storemanager.user.first_name = data['user']['first_name']
        storemanager.user.last_name = data['user']['last_name']
        storemanager.user.save()

        data = {
            'username': storemanager.user.username,
            'email': storemanager.user.email,
            'first_name': storemanager.user.first_name,
            'last_name': storemanager.user.last_name,
            'is_active': 'Activo' if storemanager.is_active else 'Inactivo'
        }

        return Response({'user': data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        user = storemanager.user
        user.delete()
        storemanager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                         Promotion Manager                             """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionManagerFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/promotionmanager/edit.html'

    def get_object(self, pk):
        try:
            return PromotionManager.objects.get(pk=pk)
        except PromotionManager.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        serializer = PromotionManagerSerializer(promotionmanager)
        data = {
            'username': serializer.data['user']['username'],
            'email': serializer.data['user']['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Activo' if serializer.data['is_active'] else 'Inactivo',
            'pk': pk
        }
        form = PromotionManagerForm()
        return Response({'form': form, 'user': data})

class PromotionManagerView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/promotionmanager/promotionmanager.html'

    def get_object(self, pk):
        try:
            return PromotionManager.objects.get(pk=pk)
        except PromotionManager.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        serializer = PromotionManagerSerializer(promotionmanager)
        data = {
            'username': serializer.data['user']['username'],
            'email': serializer.data['user']['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Activo' if serializer.data['is_active'] else 'Inactivo'
        }
        return Response({'user': data})

    def post(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        form = PromotionManagerEditForm(request.POST)
        if form.is_valid():
            data = {
                'user': {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'password': form.cleaned_data['password']
                }
            }
            serializer = PromotionManagerEditSerializer(data=data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        promotionmanager.user.set_password(data['user']['password'])
        promotionmanager.user.first_name = data['user']['first_name']
        promotionmanager.user.last_name = data['user']['last_name']
        promotionmanager.user.save()

        data = {
            'username': promotionmanager.user.username,
            'email': promotionmanager.user.email,
            'first_name': promotionmanager.user.first_name,
            'last_name': promotionmanager.user.last_name,
            'is_active': 'Activo' if promotionmanager.is_active else 'Inactivo'
        }

        return Response({'user': data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        user = promotionmanager.user
        user.delete()
        promotionmanager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                             Admin                                     """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        
class AdminView(APIView):
    def get_object(self, pk):
        try:
            return Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        admin = self.get_object(pk)
        serializer = AdminSerializer(admin)
        data = {
            'username': serializer.data['user']['username'],
            'email': serializer.data['user']['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name']
        }
        return Response({'user': data})

    def put(self, request, pk, format=None):
        admin = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)