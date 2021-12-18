from django.urls import path
from tasks import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path( 'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path( 'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh' ),
]
