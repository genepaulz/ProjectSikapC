from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    
    path('a',views.RegisterViewA.as_view(),name="registera_view"),
    path('e',views.RegisterViewE.as_view(),name="registere_view"),
    
]