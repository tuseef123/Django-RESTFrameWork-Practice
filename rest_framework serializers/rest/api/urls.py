
from django.urls import path
from . import views
urlpatterns = [
    path('api/<int:pk>/',views.student_details,name = 'home'),
    path('api/',views.student_list,),
]
