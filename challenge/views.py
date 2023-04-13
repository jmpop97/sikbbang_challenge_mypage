from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Challenge
from django.contrib.auth.decorators import login_required

# Create your views here.


def view_posting_challenge(request):
    return render(request, 'challenge/posting.html')


def posting_challenge(request):
    chellenge_title = request.POST.get('challenge_title')
    challenge_name = request.POST.get('challenge_name')
    challenge_genre = request.POST.get('challenge_genre')
    challenge_content = request.POST.get('challenge_content')
    challenge_image = request.FILES.get('challenge_image')
    challenge = Challenge(chellenge_title=chellenge_title, challenge_name=challenge_name,
                          challenge_genre=challenge_genre, challenge_content=challenge_content, challenge_image=challenge_image)
    challenge.save()

    return redirect('/challenge/posting')


def challenge_detail(request):
    pass
