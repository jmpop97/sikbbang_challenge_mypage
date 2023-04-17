from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from comments.models import CommentModel
from django.contrib.auth.decorators import login_required
from .models import ChallengeModel, ChallengeJoinModel


def view_main(request):
    challenges = ChallengeModel.objects.all()
    context = {
        'challenges': challenges
    }
    return render(request, 'main.html', context)


@login_required(login_url='/signin/')
def view_posting_challenge(request):
    return render(request, 'challenge/posting.html')


@login_required(login_url='/signin/')
def posting_challenge(request):
    if request.method == 'POST':
        challenge_author = request.user  # 현재 로그인한 유저
        challenge_title = request.POST.get('challenge_title')
        challenge_name = request.POST.get('challenge_name')
        challenge_genre = request.POST.get('challenge_genre')
        challenge_content = request.POST.get('challenge_content')
        challenge_image = request.FILES.get('challenge_image')
        if challenge_title and challenge_name and challenge_genre and challenge_content:
            challenge = ChallengeModel(challenge_author=challenge_author, challenge_title=challenge_title, challenge_name=challenge_name,
                                       challenge_genre=challenge_genre, challenge_content=challenge_content, challenge_image=challenge_image)
            challenge.save()
            challenge.mypage_key.add(request.user.id)
            challenge_id = challenge.id
            return redirect('/challenge/' + str(challenge_id) + '/')
        else:
            pass
    else:
        return redirect('/main/')


@login_required(login_url='/signin/')
def challenge_detail(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    if request.method == 'GET':
        all_comment = CommentModel.objects.filter(
            comment_challenge=target_challenge).order_by("-comment_created_at")
        user = request.user
        is_joined = ChallengeJoinModel.objects.filter(
            joined_challenge=target_challenge, joined_user=user).exists()
        is_completed = ChallengeJoinModel.objects.filter(
            joined_challenge=target_challenge, joined_user=user, complete=True).exists()
        context = {
            'challenge': target_challenge,
            'all_comment': all_comment,
            'is_joined': is_joined,
            'is_completed': is_completed,
        }
        return render(request, 'challenge/detail.html', context)
    if request.method == 'POST':
        user = request.user
        my_comment = CommentModel()
        my_comment.comment_challenge = target_challenge
        my_comment.comment_writer = user
        my_comment.comment_content = request.POST.get(
            'comment_content', '')  # 사용자가 입력한 댓글내용
        my_comment.comment_image = request.FILES.get(
            'comment_image')  # 사용자가 업로드한 이미지파일
        my_comment.save()  # 입력한 값들을 DB에 저장하는 중요한 명령어
        my_comment.mypage_key.add(user.id)
        # 저장하고 나면 댓글 보는 화면으로 보낸다.
        return redirect('/challenge/' + str(target_challenge.id) + '/')


# =========챌린지 검색 view ============
def challenge_search_view(request):
    query = request.GET.get('q')  # GET에서 파라미터 가져와서 query변수에 할당
    results = ChallengeModel.objects.filter(challenge_title__icontains=query)
    context = {'query': query, 'results': results}
    return render(request, 'challenge/challenge_search.html', context)


# =======챌린지 삭제=============
@login_required(login_url='/signin/')
def delete_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    challenge_id = target_challenge.id
    if request.user == target_challenge.challenge_author:
        target_challenge.delete()
        return redirect('/main/')
    else:
        messages.info(request, '권한이 없습니다.')
        return redirect('/challenge/' + str(challenge_id) + '/')


# =======챌린지 edit=========
@login_required(login_url='/signin/')
def edit_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    challenge_id = target_challenge.id
    if request.user == target_challenge.challenge_author:
        if request.method == 'GET':
            context = {
                'challenge': target_challenge
            }
            return render(request, 'challenge/detail_edit.html', context)

        if request.method == 'POST':
            target_challenge.challenge_title = request.POST.get(
                'challenge_title')
            target_challenge.challenge_name = request.POST.get(
                'challenge_name')
            target_challenge.challenge_genre = request.POST.get(
                'challenge_genre')
            target_challenge.challenge_content = request.POST.get(
                'challenge_content')
            target_challenge.challenge_image = request.FILES.get(
                'challenge_image') or target_challenge.challenge_image
            if target_challenge.challenge_title and target_challenge.challenge_name and target_challenge.challenge_genre and target_challenge.challenge_content:
                target_challenge.save()
                return redirect('/challenge/' + str(challenge_id) + '/')
    else:
        messages.info(request, '권한이 없습니다.')
        return redirect('/challenge/' + str(challenge_id) + '/')


@login_required(login_url='/signin/')
def comment_update(request, id):
    post_del = get_object_or_404(CommentModel, id=id)
    post = post_del.comment_challenge.id

    if request.method == "GET":
        context = {"post_del": post_del}
        return render(request, "challenge/comment_update.html", context)
    if request.method == "POST":
        post_del.comment_content = request.POST["inputValue"]
        post_del.comment_image = request.FILES.get('input_image')
        post_del.save()
    return redirect('/challenge/' + str(post) + '/')


@login_required(login_url='/signin/')
def comment_delete(request, id):
    if request.method == "POST":
        post = get_object_or_404(CommentModel, id=id)
        post_del = post.comment_challenge.id
        post.delete()

    return redirect('/challenge/' + str(post_del) + '/')


@login_required(login_url='/signin/')
def join_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    target_user = request.user
    challenge_id = target_challenge.id

    # 챌린지에 이미 참가한 경우
    if ChallengeJoinModel.objects.filter(joined_challenge=target_challenge, joined_user=target_user).exists():
        messages.info(request, '이미 참가중인 챌린지입니다.')
        return redirect('/challenge/' + str(challenge_id) + '/')

    # 챌린지에 아직 참가하지 않은 경우
    ChallengeJoinModel.objects.create(
        joined_challenge=target_challenge, joined_user=target_user)
    target_challenge.mypage_key.add(int(target_user.id))
    messages.info(request, '참가 완료!')
    return redirect('/challenge/' + str(challenge_id) + '/')


@login_required(login_url='/signin/')
def complete_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    target_user = request.user
    challenge_id = target_challenge.id

    try:
        joined_challenge = ChallengeJoinModel.objects.get(
            joined_challenge=target_challenge, joined_user=target_user)
    except ChallengeJoinModel.DoesNotExist:
        messages.info(request, '참가중인 챌린지가 아닙니다.')
        return redirect('/challenge/' + str(challenge_id) + '/')

    # 참가한 상태에서만 완료하게 하는 판별식
    if not joined_challenge.complete:
        joined_challenge.complete = True
        joined_challenge.save()
        messages.info(request, '챌린지 완료!')
        return redirect('/challenge/' + str(challenge_id) + '/')
    else:
        messages.info(request, '이미 완료한 챌린지입니다.')
        return redirect('/challenge/' + str(challenge_id) + '/')
