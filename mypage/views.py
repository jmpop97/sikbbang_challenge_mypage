from django.shortcuts import render
from .models import MyPage
from testapp.models import TestApp
# Create your views here.
def mychallenge(request):
    testkey1=MyPage.objects.get(id='5')
    print(testkey1.mypage_test.all())
    test_app_key=TestApp.objects.get(id='1')
    print(test_app_key.testname.all())
    return render(request,'mypage/mypage.html')

def mychallengeadd(request):
    testkey1 = MyPage.objects.get(id='5')
    test_app_key=TestApp.objects.get(id='5')
    testkey1.mypage_test.add('4')
    testkey1.mypage_test.remove('5')
    return render(request,'mypage/mypage.html')
