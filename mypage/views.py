from django.shortcuts import render
from .models import MyPageModel
from .forms import *
from qna.models import QnaModel
# Create your views here.
def mychallenge(request):
    testkey1=MyPageModel.objects.get(id='5')
    print(testkey1.qna_key.all())
    test_app_key=QnaModel.objects.get(id='1')
    print(test_app_key.mypage_key.all())
    return render(request,'mypage/mypage.html')

def mychallengeadd(request):
    testkey1 = MyPageModel.objects.get(id='5')
    test_app_key=QnaModel.objects.get(id='5')
    testkey1.qna_key.add('4')
    testkey1.qna_key.remove('5')
    return render(request,'mypage/mypage.html')

def mychallengeform(request):
    form1=MyPageForm1()
    # if request.method == "POST":
    #     form=MyPageForm2(request.POST)
    #     form.save()
    #     print(form)
    form2 = MyPageForm2()
    form3 = MyPageForm3()
    forms=[form1,form2,form3]
    print(forms)
    return render(request,'mypage/mypage.html',{'forms': forms})


def qna_list(request):
    qna_info=[]
    print(request.user.id)
    qna_key=MyPageModel.objects.get(id=request.user.id)
    qna_info=qna_key.qna_key.all()
    return qna_info
def mypage_list(request):
    list=qna_list(request)
    return render(request, 'mypage/mypage_list.html',{'list':list})