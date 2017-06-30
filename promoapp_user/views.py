from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import permissions, generics

from serializers import *

from django.contrib.auth.models import User as django_User

from .models import User as MyUser, Admin, StoreManager, PromotionManager

from forms import *

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Max
from django.http import Http404

# *****************************************************************************
# **********************            Login            **************************
# *****************************************************************************
class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/login.html'
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        form = LoginForm()
        return Response({'form': form})

    def post(self, request, format=None):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            u = django_User.objects.get(email=email)
            user = authenticate(username=u.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'promoapp_user/login.html', {'form': form, 'error': "Your password is incorrect!"})

        else:
            return render(request, 'promoapp_user/login.html', {'form': form})

# *****************************************************************************
# **********************           Logout            **************************
# *****************************************************************************
class Logout(APIView):
    def post(self, request, format=None):
        logout(request)
        return redirect('login')

# *****************************************************************************
# **********************           Dashboard         **************************
# *****************************************************************************
class Dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/dashboard.html'

    def get(self, request):
        """ Get the type of user that logged in """
        if StoreManager.objects.filter(user_id=request.user.pk):
            user_type = 'SM'    
        elif PromotionManager.objects.filter(user_id=request.user.pk):
            user_type = 'PM'
        elif Admin.objects.filter(user_id=request.user.pk):
            user_type = 'Admin'
        elif User.objects.filter(user_id=request.user.pk):
            user_type = 'User'
        else:
            user_type = 'Django Admin'
        return Response({'type': user_type})

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
        users = MyUser.objects.all()
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
        username = data['email'] if data['email'] != '' else data['user']['first_name'].lower() + str(mx)

        u = django_User.objects.create(username=data['user']['username']) 
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
        sm_form = PromotionManagerForm()
        user_form = DjangoUserForm()
        return Response({'sm_form': sm_form, 'user_form': user_form})

class StoreManagerListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/storemanager/storemanagers.html'
    
    """ List all store managers """
    def get(self, request, format=None):
        storemanagers = StoreManager.objects.all()
        serializer = StoreManagerSerializer(storemanagers, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        sm_form = StoreManagerForm({'email': request.POST['email']})
        user_form = DjangoUserForm({'username': request.POST['username'], 'password': request.POST['password']})
        if sm_form.is_valid() and user_form.is_valid():
            data = {
                'user': {
                    'username': user_form.cleaned_data['username'],
                    'password': user_form.cleaned_data['password']
                },
                'email': sm_form.cleaned_data['email']
            }
            u = django_User.objects.create(username=data['user']['username'])
            u.set_password(data['user']['password'])
            u.email = data['email']
            u.save()

            s = StoreManager.objects.create(user=u, email=data['email'])

            storemanagers = StoreManager.objects.all()
            serializer = StoreManagerSerializer(storemanagers, many=True)

            return Response({'users': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return render(request, 'promoapp_user/storemanager/form.html', {'sm_form': sm_form, 'user_form': user_form})

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                         Promotion Manager                             """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionManagerFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/promotionmanager/form.html'

    def get(self, request, format=None):
        pm_form = PromotionManagerForm()
        user_form = DjangoUserForm()
        return Response({'pm_form': pm_form, 'user_form': user_form})

class PromotionManagerListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_user/promotionmanager/promotionmanagers.html'

    """ List all promotion managers """
    def get(self, request, format=None):
        promotionmanagers = PromotionManager.objects.all()
        serializer = PromotionManagerSerializer(promotionmanagers, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        pm_form = PromotionManagerForm({'email': request.POST['email']})
        user_form = DjangoUserForm({'username': request.POST['username'], 'password': request.POST['password']})
        if pm_form.is_valid() and user_form.is_valid():
            data = {
                'user': {
                    'username': user_form.cleaned_data['username'],
                    'password': user_form.cleaned_data['password']
                },
                'email': pm_form.cleaned_data['email']
            }
            u = django_User.objects.create(username=data['user']['username'])
            u.set_password(data['user']['password'])
            u.email = data['email']
            u.save()

            s = PromotionManager.objects.create(user=u, email=data['email'])

            promotionmanagers = PromotionManager.objects.all()
            serializer = PromotionManagerSerializer(promotionmanagers, many=True)

            return Response({'users': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return render(request, 'promoapp_user/promotionmanager/form.html', {'pm_form': sm_form, 'user_form': user_form})

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
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
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
            'email': serializer.data['email'],
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
class StoreManagerDelete(APIView):
    def get_object(self, pk):
        try:
            return StoreManager.objects.get(pk=pk)
        except StoreManager.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        user = storemanager.user
        user.delete()
        storemanager.delete()
        return redirect('storemanagers')

class StoreManagerEditStatus(APIView):
    def get_object(self, pk):
        try:
            return StoreManager.objects.get(pk=pk)
        except StoreManager.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        storemanager = self.get_object(pk)

        try:
            is_active = True if request.POST['is_active'] == 'True' else 'False'
            storemanager.is_active = is_active
            storemanager.save()
        except:
            return Response({'is_active': 'This field is required.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        return redirect('storemanagers')        

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
            'email': serializer.data['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Active' if serializer.data['is_active'] else 'Inactive',
            'pk': pk
        }
        form = DjangoUserEditForm()
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
            'email': serializer.data['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Active' if serializer.data['is_active'] else 'Inactive',
        }
        return Response({'user': data})

    def post(self, request, pk, format=None):
        storemanager = self.get_object(pk)
        form = DjangoUserEditForm(request.POST)
        if form.is_valid():
            data = {
                'user': {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'password': form.cleaned_data['password']
                }
            }

            storemanager.user.set_password(data['user']['password'])
            storemanager.user.first_name = data['user']['first_name']
            storemanager.user.last_name = data['user']['last_name']
            storemanager.user.save()

            data = {
                'username': storemanager.user.username,
                'email': storemanager.email,
                'first_name': storemanager.user.first_name,
                'last_name': storemanager.user.last_name,
                'is_active': 'Active' if storemanager.is_active else 'Inactive'
            }

            return Response({'user': data}, status=status.HTTP_201_CREATED)
        else:
            serializer = StoreManagerSerializer(storemanager)
            data = {
                'username': serializer.data['user']['username'],
                'email': serializer.data['email'],
                'first_name': serializer.data['user']['first_name'],
                'last_name': serializer.data['user']['last_name'],
                'is_active': 'Active' if serializer.data['is_active'] else 'Inactive',
                'pk': pk
            }
            return render(request, 'promoapp_user/storemanager/edit.html', {'form': form, 'user': data})

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
class PromotionManagerDelete(APIView):
    def get_object(self, pk):
        try:
            return PromotionManager.objects.get(pk=pk)
        except PromotionManager.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        user = promotionmanager.user
        user.delete()
        promotionmanager.delete()
        return redirect('promotionmanagers')

class PromotionManagerEditStatus(APIView):
    def get_object(self, pk):
        try:
            return PromotionManager.objects.get(pk=pk)
        except PromotionManager.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)

        try:
            is_active = True if request.POST['is_active'] == 'True' else 'False'
            promotionmanager.is_active = is_active
            promotionmanager.save()
        except:
            return Response({'is_active': 'This field is required.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        return redirect('promotionmanagers')

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
            'email': serializer.data['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Active' if serializer.data['is_active'] else 'Inactive',
            'pk': pk   
        }
        form = DjangoUserEditForm()
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
            'email': serializer.data['email'],
            'first_name': serializer.data['user']['first_name'],
            'last_name': serializer.data['user']['last_name'],
            'is_active': 'Active' if serializer.data['is_active'] else 'Inactive'
        }
        return Response({'user': data})

    def post(self, request, pk, format=None):
        promotionmanager = self.get_object(pk)
        form = DjangoUserEditForm(request.POST)
        if form.is_valid():
            data = {
                'user': {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'password': form.cleaned_data['password']
                }
            }

            promotionmanager.user.set_password(data['user']['password'])
            promotionmanager.user.first_name = data['user']['first_name']
            promotionmanager.user.last_name = data['user']['last_name']
            promotionmanager.user.save()

            data = {
                'username': promotionmanager.user.username,
                'email': promotionmanager.email,
                'first_name': promotionmanager.user.first_name,
                'last_name': promotionmanager.user.last_name,
                'is_active': 'Active' if promotionmanager.is_active else 'Inactive'
            }

            return Response({'user': data}, status=status.HTTP_201_CREATED)
        else:
            serializer = PromotionManagerSerializer(promotionmanager)
            data = {
                'username': serializer.data['user']['username'],
                'email': serializer.data['email'],
                'first_name': serializer.data['user']['first_name'],
                'last_name': serializer.data['user']['last_name'],
                'is_active': 'Active' if serializer.data['is_active'] else 'Inactive',
                'pk': pk
            }
            return render(request, 'promoapp_user/promotionmanager/edit.html', {'form': form, 'user': data})

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
            'email': serializer.data['email'],
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