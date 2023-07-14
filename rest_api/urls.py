from django.urls import path
from .views import genericAPIView

urlpatterns = [
    path('genericAPIView/<int:id>',genericAPIView.as_view())
]
