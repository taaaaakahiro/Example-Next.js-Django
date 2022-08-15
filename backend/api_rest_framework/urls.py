from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet

# DefaultRouter クラスのインスタンスを代入
router = routers.DefaultRouter()
# userInfo/ にUserInfoViewSetをルーティングする
router.register('customer',CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]