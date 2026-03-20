from . import views
from django.urls import path

urlpatterns = [
    path("", views.RunList.as_view(), name='home'),
    path('<slug:slug>/', views.run_detail, name='run_detail')
]