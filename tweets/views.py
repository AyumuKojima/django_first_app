from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse
# Create your views here.
from .models import Tweet

def index(request):
    tweets = Tweet.objects.order_by('-pub_date')
    print(request.user)
    return render(request, 'tweets/index.html', {'tweets': tweets, 'user': request.user})

class DetailView(generic.DetailView):
    model = Tweet
    template_name = 'tweets/detail.html'

class EditView(generic.DetailView):
    model = Tweet
    template_name = 'tweets/edit.html'

def post(request):
    return render(request, 'tweets/post.html')

def create(request):
    tweet_data = request.POST
    error_messages = _set_error_messages(tweet_data)
    
    if len(error_messages) != 0:
        return render(request, 'tweets/post.html', { 'error_messages': error_messages })
        
    posted_tweet = Tweet(image=tweet_data['image'], text=tweet_data['text'], pub_date=timezone.now(), user=request.user)
    posted_tweet.save()
    return HttpResponseRedirect(reverse('tweets:index'))

def destroy(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    try:
        tweet.delete()
        print("Tweet <text: '" + str(tweet) + "'> is deleted successfully!")
        tweets = Tweet.objects.order_by('-pub_date')
        return render(request, 'tweets/index.html', { 'tweets': tweets })
    except:
        print('Error! Some problems are occurred.')
        return render(request, 'tweets/detail.html', { 'tweet': tweet })

def update(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet_data = request.POST
    tweet.image = tweet_data['image']
    tweet.text = tweet_data['text']
    error_messages = _set_error_messages(tweet_data)
    if len(error_messages) != 0:
        return render(request, 'tweets/edit.html', { 'tweet': tweet, 'error_messages': error_messages })
    
    try:
        tweet.save()
        print("Tweet <text: " + str(tweet) + "> is updated successfully!")
        return render(request, 'tweets/detail.html', { 'tweet': tweet })
    except:
        print("Error! Some problems are occurred!")
        return HttpResponseRedirect(reverse('tweets:detail'))


def _set_error_messages(tweet_data):
    error_messages = []
    if tweet_data['image'] == '':
        error_message = "Image URL can't be blank"
        error_messages.append(error_message)
    
    if tweet_data['text'] == '':
        error_message = "Text can't be blank"
        error_messages.append(error_message)
    
    return error_messages