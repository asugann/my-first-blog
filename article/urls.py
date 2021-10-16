from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('dragons/', views.dragons, name="dragons"),
    path('history/', views.dragonshistory, name="history")
]
