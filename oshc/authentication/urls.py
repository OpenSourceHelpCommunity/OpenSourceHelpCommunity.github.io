from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login/profile/', views.profile, name="profile"),
    url(r'^ajax/validate_username/$',
        views.validate_username,
        name='validate_username'),
]
