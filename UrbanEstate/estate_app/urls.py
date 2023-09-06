from django.urls import path
from .views import home, signup, login_view,logout_view, upload, delete_media, edit_media

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('upload/', upload, name='upload'),
    path('delete_media/<int:media_id>/', delete_media, name='delete_media'),
    path('edit_media/<int:media_id>/', edit_media, name='edit_media'),
    ]
