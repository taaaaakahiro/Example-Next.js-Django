from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Customer
from .serializer import CustomersSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Customer.objects.all() \
        .select_related('occupation_id')\
        .select_related('status_id')\
        .select_related('payment_status_id')
        

    # シリアライザーを取得
    serializer_class = CustomersSerializer


