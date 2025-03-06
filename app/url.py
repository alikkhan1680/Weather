from django.urls import path
from .views import CountryDataAPIView, Register, Login, LogoutView

urlpatterns = [
    path('country-data/', CountryDataAPIView.as_view(), name='country-data'),
    path('register/', Register.as_view(), name='reg'),
    path("login/", Login.as_view(), name="loogin"),
    path("logoute/", LogoutView.as_view(), name="logoute"),
]