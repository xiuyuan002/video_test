
from django.urls import path
from .views.base import Index
from .views.auth import Login,AdminManger,LogOut,UpdateAdminStatus
from .views.video import ExternaVideo,VideoSubView,VideoStarView,StarDelete

urlpatterns =[
    path('',Index.as_view(),name='dashboard_index'),
    path('login',Login.as_view(),name='dashboard_login'),
    path('logout',LogOut.as_view(),name='dashboard_logout'),
    path('admin/manger',AdminManger.as_view(),name='admin_manger'),
    path('admin/manger/update/status',UpdateAdminStatus.as_view(),name='admin_update_status'),
    path('video/externa',ExternaVideo.as_view(),name='externa_video'),
    path('video/videosub/<int:video_id>',VideoSubView.as_view(),name='video_sub'),
    path('video/star',VideoStarView.as_view(),name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>',StarDelete.as_view(),name='star_delete')
]