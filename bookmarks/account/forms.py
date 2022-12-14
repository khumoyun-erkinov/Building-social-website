from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm): #Biz hozir user moedli uchum forma yaratdik
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','email']


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')  #Bu parollarni tekshiradi va tozalaydi
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():           #bu esa email tekshirai
            raise forms.ValidationError('Email already in use')
        return data







class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileEditForm(forms.ModelForm): #Bu bizning profile malumotlarimza Profile modelga saqlaydi,va USer tug`ilgan kunini yoza oldai va upload qila oldi rasmi
    class Meta:
        model = Profile
        fields = ['date_of_birth','photo']





