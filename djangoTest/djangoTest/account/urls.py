from .views import CalculateSum, CalculateEquation, CalculateNextNumebrInSeries, RegisterUser
from django.urls import include, path, re_path

urlpatterns = [
    path('api/v1/calculate',
         CalculateSum.as_view(), name='get_calculate_sum'),
    path('api/v1/calculate/equation',
         CalculateEquation.as_view(), name='get_calculate_equation'),
    path('api/v1/calculate/next/number',
         CalculateNextNumebrInSeries.as_view(), name='get_calculate_next_number'),
    path('api/v1/register',
         RegisterUser.as_view(), name='register_user')
]
