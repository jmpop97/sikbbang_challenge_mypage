from django.shortcuts import render
from .models import MyPageModel
from .models import ChallengeModel
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
    print(request.user.id)
    keys=MyPageModel.objects.get(id=request.user.id)
    qna_info=keys.qna_key.all()
    return qna_info

def challenge_list(request):
    print(request.user.id)
    keys=MyPageModel.objects.get(id=request.user.id)
    challenge_info=keys.challenge_key.all()
    return challenge_info
def mypage_list(request):
    list1 = qna_list(request)
    list2 = challenge_list(request)
    lists=[list1,list2]
    return render(request, 'mypage/mypage_list.html',{'lists':lists})