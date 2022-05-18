from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Tweet

def index(request):
    tweets = Tweet.objects.order_by('-pub_date')
    return render(request, 'tweets/index.html', { 'tweets': tweets })

def detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweets/detail.html', { 'tweet': tweet })