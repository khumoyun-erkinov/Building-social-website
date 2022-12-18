from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # Form Login forimga kiradi
        if form.is_valid():# agar form valid bo`masa
            cd = form.cleaned_data # agar form tasdiqlanmagan bo`lsa tasdiqlidi yani bormi yoqmi bazada
            user = authenticate(request, # autehticate(tasdiqlash) request,username,password tasdiqldi
                                username=cd['username'],
                                password=cd['password'])
            if user is not None: # agar user mavjud bo`lmasas
                if user.is_active:# User active degan shart beramiza
                    login(request, user) #userga shart  bergandan keyin login beramza keyingi qadami
                    return HttpResponse('Muvaffaqiyatli tasdiqlandi') #qaytaradi agar yengi register qilsa
                else:
                    return HttpResponse('Ochirilgan hisoblar') #Bo`lmasa shuni qaytaradi
        else:
                return HttpResponse('Mavjud login') # agar user active bo`sa yoki bor bo`lsa qaytaradi
    else:
        form = LoginForm() #agar formi ichidigi oldin regisrer bo`lgan bo`sa login form qaytaradi
    return render(request,'account/login.html',{'form':form}) # va login.htmlga yuboradi

@login_required # BU tekshirdi user audentifikastiyadan o`tganimi yoqmi
def dashboard(request): # Agar user tasdiqlang decorate view amalga oshirad.aks xolda bo`msa userni login urlga yo`naltraadi
    return render(request,
                  'account/dashboard.html',
                  {'section':'dashboard'})

def regester(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(  #set_password database joylashdan oldin hashlida malumaoralrni qaysiiki userning
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile updated' 'successfully')
        else:
            messages.error(request,'Error updading your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(

            instance=request.user.profile
        )
    return render(request,
                  'account/edit.html',
                  {'user_form':user_form,
                   'profile_form': profile_form})











