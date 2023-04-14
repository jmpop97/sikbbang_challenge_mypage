from django import forms
from .models import MyPageModel
from qna.models import QnaModel

class MyPageForm1(forms.ModelForm):
    class Meta:
        model = MyPageModel
        fields=['qna_key']
class MyPageForm2(forms.ModelForm):
    class Meta:
        model = MyPageModel
        fields=['qna_key']
    qna_key = forms.ModelMultipleChoiceField(
        QnaModel.objects.all(),
        widget=forms.CheckboxSelectMultiple)
class MyPageForm3(forms.ModelForm):
    class Meta:
        model = MyPageModel
        fields=['qna_key']
        widgets={
            'qna_key': forms.CheckboxSelectMultiple(),
        }
