from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ChallengeModel
from django.contrib.auth.decorators import login_required

# Create your views here.


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
            challenge_id = challenge.id
            return redirect('/challenge/' + str(challenge_id))

        else:
            pass


@login_required
def challenge_detail(request, id):
    target_challenge = ChallengeModel.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'challenge': target_challenge
        }
        return render(request, 'challenge/detail.html', context)


def delete_challenge(request, id):
    target_challenge = ChallengeModel.objects.get(id=id)
    target_challenge.delete()
    return redirect('/main')
