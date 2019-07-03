from django.urls import path, register_converter,re_path

from . import views, converters

app_name = 'booktest'
register_converter(converters.FourDigitYearConverter, 'year')
urlpatterns = [
    path('', views.index, name='index'),
    path('<year:year>', views.year),
    path('<int:id>', views.show),
    # re_path(),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]
