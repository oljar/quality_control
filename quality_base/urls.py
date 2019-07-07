from django.urls import path
from . import views


app_name ='quality_control'
urlpatterns = [
    path('', views.main_report, name='main_report'),
    path('<int:year>/<int:month>/<int:day>/',
         views.detail_report,name='detail_report'),

    path('<int:year>/<int:month>/<int:day>/<person>',
         views.controller_raport, name='controller_report')

]