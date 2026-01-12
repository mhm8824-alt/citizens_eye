import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citizens_eye_1.settings') # تأكد من اسم مشروعك هنا
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '12345678')
    print("Admin user created successfully!")
else:
    print("Admin user already exists.")