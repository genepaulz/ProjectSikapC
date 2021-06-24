from django.urls import path
from . import views

app_name = 'viewas'
urlpatterns = [    
    path('a',views.ViewAsAView.as_view(),name="viewasa_view"),
    path('e',views.ViewAsEView.as_view(),name="viewase_view"),
]