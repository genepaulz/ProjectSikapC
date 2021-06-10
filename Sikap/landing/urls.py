from django.urls import path
from . import views

app_name = 'landing'
urlpatterns = [
    path('',views.LandingView.as_view(),name="landing_view"),
]