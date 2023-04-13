from django.shortcuts import render
from .models import MyPage
from qna.models import QnaModel
# Create your views here.
def mychallenge(request):
    testkey1=MyPage.objects.get(id='5')
    print(testkey1.qna_key.all())
    test_app_key=QnaModel.objects.get(id='1')
    print(test_app_key.mypage_key.all())
    return render(request,'mypage/mypage.html')

def mychallengeadd(request):
    testkey1 = MyPage.objects.get(id='5')
    test_app_key=QnaModel.objects.get(id='5')
    testkey1.qna_key.add('4')
    testkey1.qna_key.remove('5')
    return render(request,'mypage/mypage.html')
