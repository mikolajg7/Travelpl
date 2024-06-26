from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('add_post/', views.add_post, name='add_post'),
    path('logout/',views.logout_met,name='logout'),
    path('accountOptions/', views.accountOptions_met, name='accountOptions'),
    path('accountOptions/', views.accountOptions, name='accountOptions1'),
    path('home2/', views.home2, name='home2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
