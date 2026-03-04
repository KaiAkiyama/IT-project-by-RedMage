from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('records/', views.record_list, name='record_list'),
    path('records/create/', views.record_create, name='record_create'),
    path('records/<int:pk>/edit/', views.record_edit, name='record_edit'),
    path('records/<int:pk>/delete/', views.record_delete, name='record_delete'),
]