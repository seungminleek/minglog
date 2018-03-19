from django.urls import path
from .views import post_detail
urlpatterns = [
    path('post/<int:pk>/',post_detail, name="de" )
]
