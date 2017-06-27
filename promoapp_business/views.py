from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from serializers import *

from models import *

from forms import *

from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

# *****************************************************************************
# **********************         CREATE/LIST        ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                              Company                                  """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CompanyFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/company/form.html'

    def get(self, request, format=None):
        form = CompanyForm()
        return Response({'form': form})

class CompanyListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/company/companies.html'

    """ List all companies """
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({'companies': serializer.data})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            serializer = CompanyCreateSerializer(data=form.cleaned_data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data 
        
        c = Company.objects.create(is_active=True)  
        c.name = data['name']
        c.rif = data['rif']
        c.commercial_sector = data['commercial_sector']
        c.address = data['address']
        c.email = data['email']
        c.save()

        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        
        return Response({'companies': serializer.data}, status=status.HTTP_201_CREATED)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                               Store                                   """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StoreEditStatus(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        store = self.get_object(pk)

        try:
            is_active = True if request.POST['is_active'] == 'True' else 'False'
            store.is_active = is_active
            store.save()
        except:
            return Response({'is_active': 'This field is required.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        return redirect('stores')

class StoreFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/store/form.html'

    def get(self, request, format=None):
        form = StoreForm()
        return Response({'form': form})

class StoreListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/store/stores.html'

    """ List all stores """
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({'stores': serializer.data})

    def post(self, request):
        form = StoreForm(request.POST)
        if form.is_valid():
            serializer = StoreCreateSerializer(data=form.cleaned_data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data 
        
        s = Store.objects.create()  
        s.name = data['name']
        s.rif = data['rif']
        s.address = data['address']
        s.email = data['email']
        s.save()

        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        
        return Response({'stores': serializer.data}, status=status.HTTP_201_CREATED)

# *****************************************************************************
# **********************    DETAILS/UPDATE/DELETE   ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                              Company                                  """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CompanyDelete(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return redirect('companies')

class CompanyEditStatus(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        company = self.get_object(pk)

        try:
            is_active = True if request.POST['is_active'] == 'True' else 'False'
            company.is_active = is_active
            company.save()
        except:
            return Response({'is_active': 'This field is required.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        return redirect('companies')

class CompanyFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/company/edit.html'

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        form = CompanyEditForm()
        return Response({'form': form, 'company': serializer.data})

class CompanyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/company/company.html'

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response({'company': serializer.data})

    def post(self, request, pk, format=None):
        company = self.get_object(pk)
        form = CompanyEditForm(request.POST)
        if form.is_valid():
            serializer = CompanyEditSerializer(data=form.cleaned_data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        company.name = data['name']
        company.rif = data['rif']
        company.commercial_sector = data['commercial_sector']
        company.address = data['address']
        company.email = data['email']
        company.save()

        return Response({'company': data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                               Store                                   """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StoreDelete(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return redirect('stores')

class StoreFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/store/edit.html'

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        form = StoreEditForm()
        return Response({'form': form, 'store': serializer.data})
        
class StoreView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/store/store.html'

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response({'store': serializer.data, 'advertisingcampaigns': store.advertisingcampaigns.all()})

    def post(self, request, pk, format=None):
        store = self.get_object(pk)
        form = StoreEditForm(request.POST)
        if form.is_valid():
            serializer = StoreEditSerializer(data=form.cleaned_data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        store.name = data['name']
        store.rif = data['rif']
        store.address = data['address']
        store.email = data['email']
        for a in form.cleaned_data['advertisingcampaigns']:
            store.advertisingcampaigns.add(a)

        store.save()

        return Response({'store': data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)