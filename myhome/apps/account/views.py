from django.shortcuts import render, redirect, get_object_or_404,render_to_response
from .models import UserInfo
from django.contrib.auth import authenticate, login
from .forms import UserInfoForm, LoginForm, RegistrationForm, ChangepwdForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            user = authenticate(username=formdata['username'], password=formdata['password'])
            if user :
                login(request, user)
                return redirect('blog:index')
            return render(request, 'blog/account/login.html', context={'error_message': '用户名或密码输入错误'})
        return render(request, 'blog/account/login.html', context={'error_message': '请输入正确信息'})
    form = LoginForm()
    return render(request, 'blog/account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # UserInfo.objects.create(user=new_user)
            return render(request, 'blog/account/register.html', {'message1': '您已注册成功'})
        return render(request, 'blog/account/register.html', {'message': '注册失败，请重新注册'})
    form = RegistrationForm()
    return render(request, 'blog/account/register.html', {'form': form})


@login_required(login_url='account:user_login')
def change_pwd(request):
    if request.method == 'POST':
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            user = UserInfo.objects.get(username=request.POST.get('username'))
            if user :
                if check_password(request.POST.get('password'), user.password):
                    user.password = make_password(request.POST.get('new_password'))
                    user.save()
                    return redirect('blog:index')
                return render(request, 'blog/account/changepwd.html', {'message': "密码错误"})
        return render(request, 'blog/account/changepwd.html', {'message': "请按正确格式提交"})
    form = ChangepwdForm()
    return render(request, 'blog/account/changepwd.html', {'form': form})


