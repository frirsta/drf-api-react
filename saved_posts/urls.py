from django.urls import path
from saved_posts import views

urlpatterns = [
    path('saved/', views.SavePostList.as_view()),
    path('saved/<int:pk>', views.SavePostDetail.as_view()),
]
