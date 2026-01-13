from django.apps import AppConfig


class ReportsConfig(AppConfig):
    name = 'reports'





from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CoreConfig(AppConfig): # تأكد أن الاسم يطابق الموجود عندك
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core' # تأكد أن هذا هو اسم تطبيقك

    def ready(self):
        # استدعاء الدالة عند اكتمال التحميل
        post_migrate.connect(create_superuser, sender=self)

def create_superuser(sender, **kwargs):
    from django.contrib.auth.models import User # الاستيراد هنا آمن
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Done: Admin created successfully!")