from django.shortcuts import render, redirect  #장고에서 제공하는 기능 중 템플릿으로 html생성하는 render와 url로 이동하는 redirect 소환
from django.contrib.auth.decorators import login_required  # 로그인 기반 접근자격 판별기
from .models import CommentModel  # models.py의 CommentModel 함수와 연결
from django.shortcuts import get_object_or_404  #임포트 버그 걸려서 빨간 줄로 나올 수도 있음.


# Create your views here.
def comment_read(request):  # comments DB 댓글들을 모두 불러와서 html에 표시하는 함수. 표시된 댓글들 중 나의 댓글에는 수정하기와 삭제하기 버튼이 보인다.
    all_comment = CommentModel.objects.all().order_by("-comment_created_at") #커멘트모델의 모든 오브젝트를 불러오는데 오더바이 안의 순서로 불러와라. 앞에 - 썼으니 역순이라 최신글 상단
    return render(request, "comments/comment_read.html", {"all_comment": all_comment}) #렌더를 해오되, 왼쪽all_comment 오른쪽all_comment 값을 담아서 html에 보내주는 것.

@login_required    #위에서 임포트한 로그인 판별기 데코레이터
def comment_create(request):  # 작성하기 버튼 클릭 시 모든 인풋값을 받아서 comments DB에 저장하는 함수
    if request.method == 'GET':  # GET 메소드로 들어오면 댓글 작성용 화면을 보여줌
        return render(request, 'comments/comment_create.html')
    if request.method == 'POST':  # POST 메소드로 들어오면 작성한 인풋값들을 DB에 전송
        user = request.user  # 지금 계정에 로그인된 사용자 이름 가져옴
        my_comment = CommentModel()  # 댓글 모델클래스 이리와
        my_comment.comment_writer = user  # UserModel의 id값을 ForeignKey로 참조하여 로그인된 사용자에 할당

        # html에서 받은 각각 인풋값들을 DB에 넣기 위해 변수 선언
        my_comment.comment_content = request.POST.get('comment_content', '')  # 사용자가 입력한 댓글내용
        my_comment.comment_image = request.FILES.get('comment_image')  # 사용자가 업로드한 이미지파일

        my_comment.save()    #입력한 값들을 DB에 저장하는 중요한 명령어
        return redirect('/api/comments')    #저장하고 나면 댓글 보는 화면으로 보낸다.


@login_required
def comment_update(request, pk):  # 나의 댓글에 보이는 수정하기 버튼 클릭 시,... 잠깐... 수정하기 버튼 누르면 새롭게 수정할 창이 떠야 하는데?
    post_del = get_object_or_404(CommentModel, pk=pk)
    if request.method == "GET":
        context = { "post_del" : post_del }
        return render(request, "comments/comment_update.html", context)
    if request.method == "POST":
        post_del.comment_content = request.POST["inputValue"]
        post_del.comment_image = request.FILES.get('input_image')
        post_del.save()
        return redirect('/api/comments')



@login_required
def comment_delete(request, pk):
    if request.method == "POST":
        post_del = get_object_or_404(CommentModel, pk=pk)
        post_del.delete()
        return redirect("/api/comments")
