from django.urls import path
from .views import GetImages

urlpatterns = [
    path('', GetImages.as_view(), name='get_images')
]
