from django.urls import path,include
from basic_app import views

#Templat urls!

app_name = 'basic_app'

urlpatterns = [
	path('register/',views.register,name="registeration"),
	path('user_login/',views.user_login,name="user_login"),
]