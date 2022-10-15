from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    url(r'delete/', views.post_remove, name='post_remove'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)