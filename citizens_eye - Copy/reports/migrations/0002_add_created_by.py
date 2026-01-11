from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),  # تأكد إنه نفس آخر مايغريشن موجود عندك
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='created_by',
            field=models.ForeignKey(
                default=1,  # مؤقت: حدد ID لمستخدم موجود في قاعدة البيانات
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]