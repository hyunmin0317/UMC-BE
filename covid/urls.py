from django.urls import path
from covid import views

urlpatterns = [
    path('all', views.CovidViewSet.as_view()),
    path('date/<str:date>/', views.CovidDateViewSet.as_view()),
]
