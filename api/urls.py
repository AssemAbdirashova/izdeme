from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views import StatisticsListAPIView, ServiceListAPIView, ServiceDetailAPIView, StatisticsDetailAPIView, open_csv

urlpatterns = [
     path('login/', obtain_jwt_token),
     path('service/', ServiceListAPIView.as_view()),
     path('service/<int:service_id>/', ServiceDetailAPIView.as_view()),
     # path('categories/<int:category_id>/products', categoryproducts),
     path('statistics/', StatisticsListAPIView.as_view()),
     path('statistics/<int:statistics_week_id>', StatisticsDetailAPIView.as_view()),
     path('statistics/csv/', open_csv),
     path('course/', CourseListAPIView.as_view()),
     path('course/<int:course_id>/', CourseDetailAPIView.as_view()),
     # path('products/<int:product_id>/', product_detail),
     # path('users/', UserAPIView.as_view()),
     # path('orders/', OrdersListAPIView.as_view()),
     # path('orders/', OrdersListAPIView.as_view()),
     # path('login/', LoginView.as_view()),
     # path('logout/', LogoutView.as_view()),
]
