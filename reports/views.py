from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import SignUpForm
from .models import Report  # نموذج الشكوى
from .models import Report, Profile
from .forms import ProfileForm

# ----------------------------
# صفحة تسجيل الدخول
# ----------------------------
class UserLoginView(LoginView):
    template_name = 'reports/login.html'
    redirect_authenticated_user = False

    def form_invalid(self, form):
        messages.error(self.request, '❌ اسم المستخدم أو كلمة المرور خاطئة')
        return super().form_invalid(form)

    def get_success_url(self):
        return '/home/'

# ----------------------------
# صفحة تسجيل الخروج
# ----------------------------
class UserLogoutView(LogoutView):
    next_page = '/'

# ----------------------------
# الصفحة الرئيسية (محمية)
# ----------------------------
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
            # إعادة الصفحة مع عرض الأخطاء والبيانات القديمة
            return render(request, 'reports/home.html', {
                'errors': errors,
                'old': request.POST
            })

        # حفظ الشكوى في قاعدة البيانات
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


# ----------------------------
# صفحة إنشاء حساب
# ----------------------------
from django.contrib import messages

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
            messages.error(request, '❌ تأكد من صحة البيانات المدخلة')
    else:
        form = SignUpForm()

    return render(request, 'reports/signup.html', {'form': form})

# ----------------------------
# صفحة البحث
# ----------------------------
@login_required(login_url='/')
def search_view(request):
    return render(request, 'reports/search.html')





# ----------------------------
# صفحة الحساب
# ----------------------------
@login_required(login_url='/')
def profile_view(request):
    # جلب أو إنشاء البروفايل
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # جلب البيانات من الفورم
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        birthdate = request.POST.get('birthdate', '').strip()

        # تحقق من اسم المستخدم
        if not username:
            messages.error(request, 'اسم المستخدم لا يمكن أن يكون فارغاً')
        else:
            # تعديل بيانات User
            request.user.username = username
            request.user.email = email
            request.user.save()

            # تعديل تاريخ الميلاد
            profile.birthdate = birthdate if birthdate else None
            profile.save()

            messages.success(request, 'تم تحديث بياناتك بنجاح')
            return redirect('profile')  # يرجع نفس الصفحة بعد الحفظ

    # تمرير البيانات للـ template
    return render(request, 'reports/profile.html', {
        'profile': profile,
        'user': request.user
    })