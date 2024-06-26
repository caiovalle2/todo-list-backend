from django.urls import path
from login.views import Login, Register, Logout

urlpatterns = [
    path('login', Login.as_view()),
    path('register', Register.as_view()),
    path('logout', Logout.as_view()),
]