from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CommentModel
from challenge.models import ChallengeModel
