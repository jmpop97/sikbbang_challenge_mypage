from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ChallengeModel, ChallengeJoinModel
from django.contrib.auth.decorators import login_required


def view_main(request):
    challenges = ChallengeModel.objects.all()
    context = {
        'challenges': challenges
    }
    return render(request, 'main.html', context)


@login_required
def view_posting_challenge(request):
    return render(request, 'challenge/posting.html')


@login_required
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
            return redirect('/challenge/' + str(challenge_id))
        else:
            pass
    else:
        return redirect('/main')


@login_required
def challenge_detail(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    if request.method == 'GET':
        context = {
            'challenge': target_challenge
        }
        return render(request, 'challenge/detail.html', context)
    else:
        return redirect('/main')


# =========챌린지 검색 view ============
def challenge_search_view(request):
    query = request.GET.get('q')  # GET에서 파라미터 가져와서 query변수에 할당
    results = ChallengeModel.objects.filter(challenge_title__icontains=query)
    context = {'query': query, 'results': results}
    return render(request, 'challenge/challenge_search.html', context)


@login_required
def delete_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    if request.user == target_challenge.challenge_author:
        target_challenge.delete()
    else:
        return HttpResponse("권한이 없습니다.")
    return redirect('/main')


@login_required
def edit_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    if request.user == target_challenge.challenge_author:
        if request.method == 'GET':
            context = {
                'challenge': target_challenge
            }
            return render(request, 'challenge/detail_edit.html', context)

        elif request.method == 'POST':
            target_challenge.challenge_title = request.POST.get(
                'challenge_title')
            target_challenge.challenge_name = request.POST.get(
                'challenge_name')
            target_challenge.challenge_genre = request.POST.get(
                'challenge_genre')
            target_challenge.challenge_content = request.POST.get(
                'challenge_content')
            target_challenge.challenge_image = request.FILES.get(
                'challenge_image')
            if target_challenge.challenge_title and target_challenge.challenge_name and target_challenge.challenge_genre and target_challenge.challenge_content:
                target_challenge.save()
                challenge_id = target_challenge.id
                return redirect('/challenge/' + str(challenge_id))
    else:
        return HttpResponse("권한이 없습니다.")


def join_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    target_user = request.user

    # 챌린지에 이미 참가한 경우
    if ChallengeJoinModel.objects.filter(joined_challenge=target_challenge, joined_user=target_user).exists:
        return HttpResponse("이미 참가중입니다.")

    # 챌린지에 아직 참가하지 않은 경우
    ChallengeJoinModel.objects.create(
        joined_challenge=target_challenge, joined_user=target_user)

    return HttpResponse("참가 완료")


def complete_challenge(request, id):
    target_challenge = get_object_or_404(ChallengeModel, id=id)
    target_user = request.user

    try:
        joined_challenge = ChallengeJoinModel.objects.get(
            joined_challenge=target_challenge, joined_user=target_user)
    except ChallengeJoinModel.DoesNotExist:
        return HttpResponse("참가부터 하세요.")

    # 참가한 상태에서만 완료하게 하는 판별식
    if not joined_challenge.complete:
        joined_challenge.complete = True
        joined_challenge.save()
        return HttpResponse("챌린지 완료")
    else:
        return HttpResponse("이미 완료한 챌린지입니다.")
