from django.conf.urls import url
from django.urls import path

from test1 import views

urlpatterns = [
    url(r'^(sss)(\d+)$', views.show1),
    path('<int:id>', views.show),

]
