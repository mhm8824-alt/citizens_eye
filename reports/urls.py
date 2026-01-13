from django.urls import path
from .views import home_view, UserLoginView, UserLogoutView, signup_view, search_view, profile_view








from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User # استيراد موديل المستخدم
from django.http import HttpResponse

# دالة سحرية لإنشاء الحساب بمجرد فتح الرابط
def create_dr_admin(request):
    if not User.objects.filter(username='dr_admin').exists():
        User.objects.create_superuser('dr_admin', 'admin@example.com', 'Admin123456')
        return HttpResponse("<h2>تم إنشاء حساب السوبر يوزر بنجاح!</h2><p>الاسم: dr_admin <br> الباسورد: Admin123456</p>")
    else:
        return HttpResponse("<h2>الحساب موجود مسبقاً!</h2>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('make-admin-for-dr/', create_dr_admin), # الرابط السري

]




























urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),  # صفحة تسجيل الدخول
    path('signup/', signup_view, name='signup'),      # صفحة إنشاء حساب
    path('home/', home_view, name='home'),           # الصفحة الرئيسية
    path('logout/', UserLogoutView.as_view(), name='logout'),  # تسجيل الخروج
    path('search/', search_view, name='search'),  # صفحة البحث
   
    path('profile/', profile_view, name='profile'),
]