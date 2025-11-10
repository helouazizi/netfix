from django.urls import path
from . import views
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('', views.main , name='main'),
    path('logout/',views.logout_user , name='logout') ,
]


handler404 = 'main.views.custom_404'
handler500 = 'main.views.custom_500'
handler403 = 'main.views.custom_403'
handler400 = 'main.views.custom_400'