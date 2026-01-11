from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField("عنوان المشكلة", max_length=200)
    description = models.TextField("وصف المشكلة")
    location = models.CharField("الموقع", max_length=255, blank=True, null=True)  # <- هنا
    image = models.ImageField("صورة", upload_to='reports_images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مستخدم")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    # تقدر تضيف أي حقول إضافية لاحقًا، مثل رقم الهاتف أو صورة الملف الشخصي

    def __str__(self):
        return f"{self.user.username} Profile"