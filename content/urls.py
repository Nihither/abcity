from django.urls import path
from .views import index, video_content_list, video_page


urlpatterns = [
    path('', index, name='index'),
    path('video/', video_content_list, name='video_list'),
    path('video/<int:video_id>/', video_page, name='video_page'),
]
