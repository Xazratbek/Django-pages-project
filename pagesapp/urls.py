from django.urls import path
from .views import HomePageView, AboutPageView,ProgrammingPageView

urlpatterns = [
    path('programming/',ProgrammingPageView.as_view(),name='programming'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('',HomePageView.as_view(),name='home'),
]