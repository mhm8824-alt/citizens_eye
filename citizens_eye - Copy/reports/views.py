from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm
from django.contrib import messages
from .models import Report  # نسيت تضيف الاستيراد للموديل

# صفحة تسجيل الدخول
class UserLoginView(LoginView):
    template_name = 'reports/login.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        return '/home/'

# صفحة تسجيل الخروج
class UserLogoutView(LogoutView):
    next_page = '/'

# الصفحة الرئيسية محمية
@login_required(login_url='/')
def home_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        location = request.POST.get('location', '').strip()
        image = request.FILES.get('image')

        errors = {}
        if not title:
            errors['title'] = 'الحقل فارغ'
        if not description:
            errors['description'] = 'الحقل فارغ'
        if not location:
            errors['location'] = 'الحقل فارغ'

        if errors:
            return render(request, 'reports/home.html', {
                'errors': errors,
                'old': request.POST
            })

        # هون التخزين لما كلشي تمام
        Report.objects.create(
            title=title,
            description=description,
            location=location,
            image=image,
            created_by=request.user
        )

        messages.success(request, '✅ تم استلام الشكوى بنجاح')
        return redirect('/home/')

    return render(request, 'reports/home.html')

# صفحة إنشاء حساب
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'reports/signup.html', {'form': form})

# صفحة البحث (فارغة حالياً)
@login_required(login_url='/')
def search_view(request):
    return render(request, 'reports/search.html')  # راح نعمل القالب بعدين




# صفحة الحساب
@login_required(login_url='/')
def profile_view(request):
    return render(request, 'reports/profile.html')