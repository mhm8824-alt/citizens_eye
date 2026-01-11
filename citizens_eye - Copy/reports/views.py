from django.shortcuts import render, redirect
from .models import Report
from django.contrib.auth.decorators import login_required

@login_required # لضمان أن المستخدم مسجل دخول قبل الإرسال
def home_view(request):
    if request.method == "POST":
        # جلب البيانات من الفورم الموجود في HTML الخاص بك
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        image = request.FILES.get('image')

        # حفظ البيانات في قاعدة البيانات SQLite
        Report.objects.create(
            title=title,
            description=description,
            location=location,
            image=image,
            created_by=request.user # حفظ الشخص الذي أرسل الشكوى
        )
        return redirect('search') # توجيهه لصفحة التتبع بعد الإرسال
    
    return render(request, 'home.html')