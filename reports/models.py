from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    # خيارات الحالة كما في المخطط المفاهيمي
    STATUS_CHOICES = [
        ('جديدة', 'جديدة'),
        ('قيد المعالجة', 'قيد المعالجة'),
        ('تم الحل', 'تم الحل'),
        ('مرفوضة', 'مرفوضة'),
    ]

    title = models.CharField("عنوان المشكلة", max_length=200)
    description = models.TextField("وصف المشكلة")
    location = models.CharField("الموقع", max_length=255, blank=True, null=True)
    image = models.ImageField("صورة", upload_to='reports_images/', blank=True, null=True)
    
    # إضافة حقل الحالة ليتطابق مع المخططات
    status = models.CharField(
        "حالة الشكوى", 
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='جديدة'
    )
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مستخدم")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # تعديل لظهار الحالة بجانب العنوان في لوحة التحكم
        return f"{self.title} ({self.status})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"