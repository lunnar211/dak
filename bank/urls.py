from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^profiles/', include("profiles.urls")),
    re_path(r'^accounts/logout/$', views.logout_view, name='logout'),
]
