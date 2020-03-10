from django.urls import path
from qapp import views

app_name = 'qapp'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
