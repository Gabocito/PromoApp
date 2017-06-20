from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from serializers import *

from models import *

from forms import *

from django.shortcuts import get_object_or_404
from django.http import Http404

# *****************************************************************************
# **********************         CREATE/LIST        ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                             Promotion                                 """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/promotion/form.html'

    def get(self, request, format=None):
        form = PromotionForm()
        return Response({'form': form})

class PromotionListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/promotion/promotions.html'

    """ List all promotions """
    def get(self, request, format=None):
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)
        return Response({'promotions': serializer.data})

    def post(self, request):
        form = PromotionForm(request.POST)
        if form.is_valid():
            serializer = PromotionSerializer(data=form.cleaned_data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data 
        
        p = Promotion.objects.create()  
        p.description = data['description']
        p.discount = data['discount']
        p.products = data['products']
        p.save()

        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)
        
        return Response({'promotions': serializer.data}, status=status.HTTP_201_CREATED)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                       Advertising Campaign                            """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class AdvertisingCampaignFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/advertisingcampaign/form.html'

    def get(self, request, format=None):
        form = AdvertisingCampaignForm()
        return Response({'form': form})

class AdvertisingCampaignListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/advertisingcampaign/advertisingcampaigns.html'

    """ List all advertising campaigns """
    def get(self, request, format=None):
        advertisingcampaigns = AdvertisingCampaign.objects.all()
        serializer = AdvertisingCampaignSerializer(advertisingcampaigns, many=True)
        return Response({'advertisingcampaigns': serializer.data})

    def post(self, request):
        form = AdvertisingCampaignForm(request.POST)
        if form.is_valid():
            serializer = AdvertisingCampaignCreateSerializer(data=form.cleaned_data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data 
        
        a = AdvertisingCampaign.objects.create()  
        a.target = data['target']
        a.start_date = data['start_date']
        a.end_date = data['end_date']
        a.save()

        advertisingcampaigns = AdvertisingCampaign.objects.all()
        serializer = AdvertisingCampaignSerializer(advertisingcampaigns, many=True)
        
        return Response({'advertisingcampaigns': serializer.data}, status=status.HTTP_201_CREATED)

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
# """                             Promotion                                 """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/promotion/edit.html'

    def get_object(self, pk):
        try:
            return Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promotion = self.get_object(pk)
        serializer = PromotionSerializer(promotion)
        form = PromotionForm()
        return Response({'form': form, 'promotion': serializer.data})

class PromotionView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/promotion/promotion.html'

    def get_object(self, pk):
        try:
            return Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promotion = self.get_object(pk)
        serializer = PromotionSerializer(promotion)
        return Response({'promotion': serializer.data})

    def post(self, request, pk, format=None):
        promotion = self.get_object(pk)
        form = PromotionEditForm(request.POST)
        if form.is_valid():
            serializer = PromotionEditSerializer(data=form.cleaned_data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        promotion.description = data['description']
        promotion.discount = data['discount']
        promotion.products = data['products']
        promotion.save()

        return Response({'promotion': data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        promotion = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        promotion = self.get_object(pk)
        promotion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                       Advertising Campaign                            """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class AdvertisingCampaignFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/advertisingcampaign/edit.html'

    def get_object(self, pk):
        try:
            return AdvertisingCampaign.objects.get(pk=pk)
        except AdvertisingCampaign.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        serializer = AdvertisingCampaignSerializer(advertisingcampaign)
        form = AdvertisingCampaignForm()
        return Response({'form': form, 'advertisingcampaign': serializer.data})

class AdvertisingCampaignView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/advertisingcampaign/advertisingcampaign.html'

    def get_object(self, pk):
        try:
            return AdvertisingCampaign.objects.get(pk=pk)
        except AdvertisingCampaign.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        serializer = AdvertisingCampaignSerializer(advertisingcampaign)
        return Response({'advertisingcampaign': serializer.data})

    def post(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        form = AdvertisingCampaignEditForm(request.POST)
        if form.is_valid():
            serializer = AdvertisingCampaignEditSerializer(data=form.cleaned_data)

            # Check format and unique constraint 
            if not serializer.is_valid(): 
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data
        advertisingcampaign.target = data['target']
        advertisingcampaign.start_date = data['start_date']
        advertisingcampaign.end_date = data['end_date']
        advertisingcampaign.save()

        return Response({'advertisingcampaign': data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        advertisingcampaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                              Company                                  """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
        form = CompanyForm()
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
        form = StoreForm()
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
        return Response({'store': serializer.data})

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