from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CommentModel  # DH 필요한 데이터 모델들


# Create your views here.

def comment_read(request):  # comments DB 댓글들을 모두 불러와서 html에 표시하는 함수. 표시된 댓글들 중 나의 댓글에는 수정하기와 삭제하기 버튼이 보인다.
    pass


@login_required
def comment_create(request):  # 작성하기 버튼 클릭 시 모든 인풋값을 받아서 comments DB에 저장하는 함수
    if request.method == 'GET':  # GET 메소드로 들어오면 댓글 작성용 화면을 보여줌
        return render(request, 'comments/comment_create.html')
    if request.method == 'POST':  # POST 메소드로 들어오면 작성한 인풋값들을 DB에 전송
        user = request.user  # 지금 계정에 로그인된 사용자 이름 가져옴 fk 써야 하나?
        my_comment = CommentModel()  # 댓글 모델클래스 이리와
        my_comment.comment_writer = user  # models.py에서 foreign key로 가져온 users테이블의 user를 author로 설정

        # html에서 받은 각각 인풋값들을 DB에 넣기 위해 변수 선언
        my_comment.comment_content = request.POST.get('comment_content', '')  # 사용자가 입력한 댓글내용
        my_comment.comment_image = request.POST.get('comment_image', '')  # 사용자가 업로드한 이미지파일

        my_comment.save()
        return redirect('/api/comments')


def comment_update(request):  # 나의 댓글에 보이는 수정하기 버튼 클릭 시,... 잠깐... 수정하기 버튼 누르면 새롭게 수정할 창이 떠야 하는데?
    pass


def comment_delete(request):
    pass
