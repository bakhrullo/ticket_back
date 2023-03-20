from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/user/create/', UserCreateView.as_view()),
    path('api/v1/user/get/<int:tg_id>', UserGetView.as_view()),
    path('api/v1/sector/', SectorListView.as_view()),
    path('api/v1/calls/', CallsGetView.as_view()),
    path('api/v1/row/', RowListView.as_view()),
    path('api/v1/order/create/', OrderCreateView.as_view()),
    path('api/v1/order/get/', OrderGetView.as_view()),
    path('api/v1/place/', PlaceListView.as_view()),
    path('api/v1/place/<int:id>', PlaceGetView.as_view()),
    path('api/v1/about/', AboutUsGetView.as_view()),
]
