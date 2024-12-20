from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detalle del post
    path('add-post/', views.add_post, name='add_post'),  # Crear post
]
