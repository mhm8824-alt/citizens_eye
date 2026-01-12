import os
import django

# سنحاول البحث عن ملف الإعدادات تلقائياً
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citizens_eye.settings') # جرب حذف _1
try:
    django.setup()
except ModuleNotFoundError:
    # إذا لم ينجح، جرب الاسم الآخر الذي قد يكون هو الصحيح
    os.environ['DJANGO_SETTINGS_MODULE'] = 'citizens_eye_1.settings' 
    django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '12345678')
    print("Admin user created successfully!")