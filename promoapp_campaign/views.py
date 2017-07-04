from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from serializers import *

from permissions import *

from models import *

from forms import *

from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

# *****************************************************************************
# **********************         CREATE/LIST        ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                             Promotion                                 """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/promotion/form.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get(self, request, format=None):
        form = PromotionForm()
        return Response({'form': form})

class PromotionListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/promotion/promotions.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

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
        else:
            return render(request, 'promoapp_campaign/promotion/form.html', {'form': form})

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                       Advertising Campaign                            """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class AdvertisingCampaignFormCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/advertisingcampaign/form.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get(self, request, format=None):
        form = AdvertisingCampaignForm()
        return Response({'form': form})

class AdvertisingCampaignListCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/advertisingcampaign/advertisingcampaigns.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

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
            
            a = AdvertisingCampaign.objects.create(start_date=data['start_date'], end_date=data['end_date'])  
            a.target = data['target']
            a.save()

            advertisingcampaigns = AdvertisingCampaign.objects.all()
            serializer = AdvertisingCampaignSerializer(advertisingcampaigns, many=True)

            return Response({'advertisingcampaigns': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return render(request, 'promoapp_campaign/advertisingcampaign/form.html', {'form': form})

# *****************************************************************************
# **********************    DETAILS/UPDATE/DELETE   ***************************
# *****************************************************************************

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """                             Promotion                                 """
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PromotionDelete(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        promotion = self.get_object(pk)
        promotion.delete()
        return redirect('promotions')

class PromotionEditStatus(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        promotion = self.get_object(pk)

        try:
            is_active = True if request.POST['is_active'] == 'True' else 'False'
            promotion.is_active = is_active
            promotion.save()
        except:
            return Response({'is_active': 'This field is required.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        return redirect('promotions')

class PromotionFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/promotion/edit.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promotion = self.get_object(pk)
        serializer = PromotionSerializer(promotion)
        form = PromotionEditForm()
        return Response({'form': form, 'promotion': serializer.data})

class PromotionView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/promotion/promotion.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

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
        else:
            serializer = PromotionSerializer(promotion)
            return render(request, 'promoapp_campaign/promotion/edit.html', {'form': form, 'promotion': serializer.data})

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
class AdvertisingCampaignRemovePromotion(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk, obj):
        if obj == 'AdvertisingCampaign':
            try:
                return AdvertisingCampaign.objects.get(pk=pk)
            except AdvertisingCampaign.DoesNotExist:
                raise Http404
        else:
            try:
                return Promotion.objects.get(pk=pk)
            except Promotion.DoesNotExist:
                raise Http404

    def post(self, request, pk, promotion, format=None):
        advertisingcampaign = self.get_object(pk, 'AdvertisingCampaign')
        promotion = self.get_object(promotion, 'Promotion')
        for p in advertisingcampaign.promotions.all():
            if p == promotion:
                advertisingcampaign.promotions.remove(p)
        advertisingcampaign.save()
        return redirect('advertisingcampaign', pk=pk)

class AdvertisingCampaignDelete(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return AdvertisingCampaign.objects.get(pk=pk)
        except AdvertisingCampaign.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        advertisingcampaign.delete()
        return redirect('advertisingcampaigns')

class AdvertisingCampaignEditStatus(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return AdvertisingCampaign.objects.get(pk=pk)
        except AdvertisingCampaign.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)

        try:
            is_active = True if request.POST['is_active'] == 'True' else 'False'
            advertisingcampaign.is_active = is_active
            advertisingcampaign.save()
        except:
            return Response({'is_active': 'This field is required.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        return redirect('advertisingcampaigns')

class AdvertisingCampaignFormEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/advertisingcampaign/edit.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return AdvertisingCampaign.objects.get(pk=pk)
        except AdvertisingCampaign.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        serializer = AdvertisingCampaignSerializer(advertisingcampaign)
        form = AdvertisingCampaignEditForm()
        return Response({'form': form, 'advertisingcampaign': serializer.data})

class AdvertisingCampaignView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'promoapp_campaign/advertisingcampaign/advertisingcampaign.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isAdminOrPromotionManager)

    def get_object(self, pk):
        try:
            return AdvertisingCampaign.objects.get(pk=pk)
        except AdvertisingCampaign.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        advertisingcampaign = self.get_object(pk)
        serializer = AdvertisingCampaignSerializer(advertisingcampaign)
        return Response({'advertisingcampaign': serializer.data, 'promotions': advertisingcampaign.promotions.all()})

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
            for p in form.cleaned_data['promotions']:
                advertisingcampaign.promotions.add(p)

            advertisingcampaign.save()

            return redirect('advertisingcampaign', pk=pk)
        else:
            serializer = AdvertisingCampaignSerializer(advertisingcampaign)
            return render(request, 'promoapp_campaign/advertisingcampaign/edit.html', {'form': form, 'advertisingcampaign': serializer.data})

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
