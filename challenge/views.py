from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ChallengeModel
from django.contrib.auth.decorators import login_required

# Create your views here.


def view_posting_challenge(request):
    return render(request, 'challenge/posting.html')


def posting_challenge(request):

    if request.method == 'POST':
        challenge_title = request.POST.get('challenge_title')
        challenge_name = request.POST.get('challenge_name')
        challenge_genre = request.POST.get('challenge_genre')
        challenge_content = request.POST.get('challenge_content')
        challenge_image = request.FILES.get('challenge_image')
        challenge = ChallengeModel(challenge_title=challenge_title, challenge_name=challenge_name,
                                   challenge_genre=challenge_genre, challenge_content=challenge_content, challenge_image=challenge_image)
        challenge.save()

        return redirect('/challenge/posting')


def challenge_detail(request, id):
    target_challenge = ChallengeModel.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'challenge': target_challenge
        }
        return render(request, 'challenge/detail.html', context)
