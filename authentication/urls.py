from django.urls import path
from authentication.views import (
    register,
    login_view,
    logout_view)
from calories.views import (home)
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),

]
