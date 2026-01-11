from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'كلمة المرور'}),
        label="كلمة المرور"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تأكيد كلمة المرور'}),
        label="تأكيد كلمة المرور"
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'اسم المستخدم'}),
            'email': forms.EmailInput(attrs={'placeholder': 'البريد الإلكتروني'}),
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("كلمتا المرور غير متطابقتين")
        return password2

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label='اسم المستخدم')
    email = forms.EmailField(required=True, label='البريد الإلكتروني')

    class Meta:
        model = Profile
        fields = ['birthdate']  # الحقول الخاصة بالـ Profile

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        user = profile.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile