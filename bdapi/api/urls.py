from django.urls import path 
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('all/',views.all, name="all-members"),
    path('one/<str:id>/',views.one, name="detail-view"),
    path('create/',views.create, name='create-member'),
    path('update/<str:id>/',views.update, name='update-member'),
    path('delete/<str:id>/',views.delete, name='delete-member'),
]
