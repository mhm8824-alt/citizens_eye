from django.db import models
from django.contrib.auth.models import User




class Report(models.Model):
    # خيارات الحالة كما في ملف الوورد (تتبع الشكوى)
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('in_progress', 'قيد المعالجة'),
        ('resolved', 'تم الحل'),
    ]

    title = models.CharField("عنوان المشكلة", max_length=200)
    description = models.TextField("وصف المشكلة")
    location = models.CharField("الموقع", max_length=255, blank=True, null=True)
    image = models.ImageField("صورة", upload_to='reports_images/', blank=True, null=True)
    
    # ربط الشكوى بالمستخدم (حفظ الحساب)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المواطن")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # حقل الحالة ليظهر في صفحة التتبع (Search)
    status = models.CharField("حالة الشكوى", max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.title} - {self.created_by.username}"