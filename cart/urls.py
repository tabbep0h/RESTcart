from django.contrib import admin
from django.urls import path
from RESTcartAPP import CRUDCart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', CRUDCart.as_view()),
    path('cart/<int:pk>/', CRUDCart.as_view())
]
