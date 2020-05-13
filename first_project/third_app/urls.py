from django.urls import path
from . import views

app_name = 'third_app'

urlpatterns=[
    path('',views.base,name="base"),
    path('scm/',views.scm,name="scm"),
    path('dba/',views.dba,name="dba"),
]
