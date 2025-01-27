from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #Course view
    path('',views.main_page,  name='course_list'),
    path('course_detail/<int:pk>/', views.course_detail_view, name='course_detail'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)