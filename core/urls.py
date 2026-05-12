from django.urls import path
from . import views
urlpatterns = [
    path('', views.dom, name='home'),
    path('education/', views.ycheba, name='education'),
    path('task1018/', views.staty, name='task_1018'),
    path('monitoring/', views.monitor, name='monitoring'),
    path('page/<slug:slug>/', views.info_str, name='dynamic_page'),
]
