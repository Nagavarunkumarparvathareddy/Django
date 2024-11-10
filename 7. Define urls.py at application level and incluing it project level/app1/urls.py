from django.urls import path
from app1.views import applicatioview

urlpatterns = [
    path('urlatapplevel/',applicatioview)
]