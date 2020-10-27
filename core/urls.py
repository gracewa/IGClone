from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>/", views.photo_detail, name="photo_detail"),
    path(r'search/', views.search_results, name='search_results'),
    path(r'accounts/profile/', views.update_profile, name='update_profile'),
    path('upload/', views.image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),

]