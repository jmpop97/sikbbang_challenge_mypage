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
