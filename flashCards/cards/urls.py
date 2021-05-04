from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('cards/', views.CollectionList.as_view()),
]
