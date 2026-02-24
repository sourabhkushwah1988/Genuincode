from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('course_inner/', views.course_inner, name='course_inner'),
    path('course/', views.course, name='course'),
    path('home/', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('base/',views.base,name='base'),
    path('learnmore_home/',views.learnmore_home,name='learnmore_home'),
    path('success/', views.success, name='success'), 
    path('my_course/', views.my_course, name='my_course'), 
    path('update-profile/', views.update_profile, name='update_profile'),
    path('logout/', logout_view, name='logout'),
    path('logout/', views.logout_view, name='logout'),
    # path('login/', views.login_view, name='login')
    
    

]
