

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("crm/", include("apps.crm.urls")),
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls")),
    

]
