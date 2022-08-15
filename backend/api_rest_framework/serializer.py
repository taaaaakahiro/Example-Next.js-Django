from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Customer

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # json で出力するフィールド
        fields = (
            'id',
            'pw',
            'fullname',
            'fullname_kana',
            'mail',
            'tel',
            'age',
            'line_name',
            'discord_name',
            'discord_id',
            'afiliate_code',
            'occupation_id',
            'payment_id',
            'prefecture_id',
            'status_id',
            'fx',
            'payment_status_id',
            'stock',
        )