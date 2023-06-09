from django.urls import path

from .import views

app_name='videos'

urlpatterns=[
    #path('recup',recup_view, name='recup'),
    #path('process/',process_view,name='process'),

    path('', views.Youtube_videoListView.as_view(), name='all'),
    path('yt/<int:pk>', views.Youtube_videoDetailView.as_view(), name='youtube_detail'),
]