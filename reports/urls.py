from django.urls import path
from .views import home_view, UserLoginView, UserLogoutView, signup_view, search_view, profile_view

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),  # صفحة تسجيل الدخول
    path('signup/', signup_view, name='signup'),      # صفحة إنشاء حساب
    path('home/', home_view, name='home'),           # الصفحة الرئيسية
    path('logout/', UserLogoutView.as_view(), name='logout'),  # تسجيل الخروج
    path('search/', search_view, name='search'),  # صفحة البحث
   
    path('profile/', profile_view, name='profile'),
]