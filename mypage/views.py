from django.shortcuts import render
from .models import MyPageModel
from .forms import *
from qna.models import QnaModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def mychallenge(request):
    testkey1 = MyPageModel.objects.get(id='5')
    print(testkey1.qna_key.all())
    test_app_key = QnaModel.objects.get(id='1')
    print(test_app_key.mypage_key.all())
    return render(request, 'mypage/mypage.html')


def mychallengeadd(request):
    testkey1 = MyPageModel.objects.get(id='5')
    test_app_key = QnaModel.objects.get(id='5')
    testkey1.qna_key.add('4')
    testkey1.qna_key.remove('5')
    return render(request, 'mypage/mypage.html')


def mychallengeform(request):
    form1 = MyPageForm1()
    # if request.method == "POST":
    #     form=MyPageForm2(request.POST)
    #     form.save()
    #     print(form)
    form2 = MyPageForm2()
    form3 = MyPageForm3()
    forms = [form1, form2, form3]
    print(forms)
    return render(request, 'mypage/mypage.html', {'forms': forms})


def qna_list(request):
    qna_info = []
    qna_key = MyPageModel.objects.get(id=request.user.id)
    qna_info = qna_key.qna_key.all()
    return qna_info



def challeng_list(request):
    challeng_info = []
    challeng_key = MyPageModel.objects.get(id=request.user.id)
    challeng_info = challeng_key.challenge_key.all()
    return challeng_info


def comment_list(request):
    comment_info = []
    comment_key = MyPageModel.objects.get(id=request.user.id)
    comment_info = comment_key.challenge_key.all()
    return comment_info

def page_list(list,list_num : int, page : int):
    paginator = Paginator(list, list_num)  # all_qna에 저장된 객체들을 10개씩 나눔
    try:  # 현재 보여줄 페이지에 해당하는 QnaModel 객체들을 가져와 qna_list에 저장
        result = paginator.page(page)
    except PageNotAnInteger:  # 'page'값이 없는 경우 'PageNotAnInteger' 예외 발생
        result = paginator.page(1)  # 1페이지 보여주기
    except EmptyPage:  # 'page'값에 임의의 값을 입력하여 요청하였을 때, 현재 페이지 범위를 초과하는 경우
        result = paginator.page(paginator.num_pages)
    return result
def mypage_list(request):
    list1 = qna_list(request)
    list2 = challeng_list(request)
    list3 = comment_list(request)
    page1 = request.GET.get('page1')
    page2 = request.GET.get('page2')
    page3 = request.GET.get('page3')

    page_limit=3
    pagelist1=page_list(list1,page_limit,page1)
    pagelist2 = page_list(list2, page_limit, page2)
    pagelist3 = page_list(list1, page_limit, page1)
    lists = [pagelist1, pagelist2, pagelist3]
    return render(request, 'mypage/mypage_list.html', {'lists': lists})
