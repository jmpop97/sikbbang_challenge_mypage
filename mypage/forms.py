from django import forms
from .models import MyPage
from qna.models import QnaModel

class MyPageForm1(forms.ModelForm):
    class Meta:
        model = MyPage
        fields=['name','qna_key']
class MyPageForm2(forms.ModelForm):
    class Meta:
        model = MyPage
        fields=['name','qna_key']
    qna_key = forms.ModelMultipleChoiceField(
        QnaModel.objects.all(),
        widget=forms.CheckboxSelectMultiple)
class MyPageForm3(forms.ModelForm):
    class Meta:
        model = MyPage
        fields=['name','qna_key']
        widgets={
            'qna_key': forms.CheckboxSelectMultiple(),
        }
