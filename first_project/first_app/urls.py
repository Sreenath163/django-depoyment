from django.urls import path
from first_app import views

urlpatterns = [
    path('index3/',views.index3,name='index3'),
    path('index4/',views.index4,name='index4'),
    path('index5/',views.index5,name='index5'),
    path('index6/',views.index6,name='index6'),
    path('index7/',views.index7,name='index7'),
    path('index8/',views.index8,name='index8'),
    path('',views.index2,name='index2'),
]
