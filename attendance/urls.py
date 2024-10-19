from django.urls import path
from attendance import views
urlpatterns = [
    path('', views.attendance, name='attendance'),
]