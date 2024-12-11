from django.urls import path

# from helloProject.urls import urlpatterns
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]