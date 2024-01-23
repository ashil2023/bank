from bankproject import settings
from . import views
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [

    path('',views.home,name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('forum/', views.forum, name='forum'),







]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)