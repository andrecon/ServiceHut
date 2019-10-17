from django.urls import path, include
from . import views
from . import philan



urlpatterns = [
		path('', views.GalleryView.as_view(), name='index'),
		#path('philanthropy/', philan.index),
		path('philanthropy/', philan.EventView.as_view(), name='philanthropy'),
		path('post/', philan.CreateEventView.as_view()),
		path('photoPost/',views.CreateImageView.as_view()),
		path('signup/', views.SignUp.as_view(), name='signup'),
]