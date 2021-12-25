from django.urls import path
from . import views

urlpatterns = [
    path('getRecom/', views.getRecomRecipe),
    path('postimages/',views.postImages ,name='postImages'),
]