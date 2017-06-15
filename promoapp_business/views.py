from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from serializers import *

from models import *

# *****************************************************************************
# **********************         CREATE/LIST        ***************************
# *****************************************************************************
class PromotionListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/promotion/promotions.html'

    """ List all promotions """
    def get(self, request, format=None):
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PromotionCreateSerializer(data=request.data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data

        p = Promotion.objects.create(name=data['name'])
        p.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AdvertisingCampaignListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/advertisingcampaign/advertisingcampaigns.html'

    """ List all advertising campaigns """
    def get(self, request, format=None):
        advertisingcampaigns = AdvertisingCampaign.objects.all()
        serializer = AdvertisingCampaignSerializer(advertisingcampaigns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisingCampaignCreateSerializer(data=request.data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data

        p = AdvertisingCampaign.objects.create(name=data['name'])
        p.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CompanyListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/company/companies.html'

    """ List all companies """
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanyCreateSerializer(data=request.data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data

        c = Company.objects.create(name=data['name'])
        c.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StoreListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_business/store/stores.html'

    """ List all stores """
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreCreateSerializer(data=request.data)

        # Check format and unique constraint 
        if not serializer.is_valid(): 
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST) 

        data = serializer.data

        s = Store.objects.create(name=data['name'])
        s.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# *****************************************************************************
# **********************    DETAILS/UPDATE/DELETE   ***************************
# *****************************************************************************
class Promotion(APIView):
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
        return Response(serializer.data)

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

class AdvertisingCampaign(APIView):
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
        return Response(serializer.data)

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

class Company(APIView):
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
        return Response(serializer.data)

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

class Store(APIView):
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
        return Response(serializer.data)

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