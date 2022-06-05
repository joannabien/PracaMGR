from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('download-images', views.download, name='download'),
    path('show', views.show, name='dupa'),
    
]