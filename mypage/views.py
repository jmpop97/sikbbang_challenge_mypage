from django.shortcuts import render
from .models import MyPage
from testapp.models import TestApp
# Create your views here.
def mychallenge(request):
    testkey1=MyPage.objects.get(id='5')
    print(testkey1.mypage_test.all())
    test_app_key=TestApp.objects.get(id='5')
    print(test_app_key.testname.all())
    return render(request,'mypage/mypage.html')