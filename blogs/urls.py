from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('viewpost/<int:post_id>/', views.viewpost, name='viewpost'),
    path('ikz_data/', views.ikz_data, name='ikz_data')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)