from django.contrib import admin
from .models import Report, Profile

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    # 1. تحديد الأعمدة التي تظهر في جدول الإدارة الرئيسي
    list_display = ('title', 'location', 'status', 'created_at', 'created_by')
    
    # 2. السماح بتعديل الحالة مباشرة من الجدول دون الدخول لكل شكوى
    list_editable = ('status',)
    
    # 3. إضافة فلاتر جانبية للتصفية حسب الحالة أو التاريخ
    list_filter = ('status', 'created_at', 'location')
    
    # 4. إضافة مربع بحث للبحث بالعنوان أو الوصف
    search_fields = ('title', 'description')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthdate')