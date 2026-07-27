from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_eventos, name='lista_eventos'),
    path('agenda/', views.lista_eventos, name='lista_eventos'),
    path('deletar/<int:id>/', views.deletar_evento, name='deletar_evento'),
]