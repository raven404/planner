from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.detail ,name="details" ),
    path('room', views.rooms ,name="room_details" ),
    path('create', views.new ,name="create" ),

]