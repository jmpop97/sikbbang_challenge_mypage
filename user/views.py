from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserUpErro
from mypage.models import MyPageModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
# 사용자가 있는지 검사하는 함수
from django.contrib.auth.decorators import login_required


def signup(request):
    form = UserUpErro()
    if request.method == 'GET':  # GET 메서드로 요청이 들어 올 경우
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html', {"form": form})
    elif request.method == 'POST':
        form = UserUpErro(request.POST)
        if form.is_valid():
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            password2 = request.POST.get('password2', None)
            if password != password2:
                messages.info(request, '비밀번호가 일치하지 않습니다.')
                return render(request, 'user/signup.html')
            else:
                exist_user = get_user_model().objects.filter(username=username)
                if exist_user:
                    # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
                    return render(request, 'user/signup.html', {"form": form})
                else:
                    UserModel.objects.create_user(
                        username=username, password=password, email=email)
                    # mypage추가
                    create_id = UserModel.objects.get(username=username)
                    mypage = MyPageModel(user_key=create_id)
                    mypage.save()
                    messages.info(request, '회원가입 완료!')
                    return redirect('/signin/')  # 회원가입이 완료되었으므로 로그인 페이지로 이동
        else:
            print(form.errors)
    return render(request, 'user/signup.html', {"form": form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username,
                               password=password)  # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, me)
            return redirect('/')
        else:  # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            messages.info(request, '아이디 또는 비밀번호를 확인해주세요.')
            return redirect('/signin/')
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect('/signin/')
