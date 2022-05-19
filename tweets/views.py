from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse
# Create your views here.
from .models import Tweet

class IndexView(generic.ListView):
    template_name = 'tweets/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Tweet
    template_name = 'tweets/detail.html'

def post(request):
    return render(request, 'tweets/post.html')

def create(request):
    data = request.POST
    error_messages = []
    if data['name'] == '':
        error_message = "Name can't be blank"
        error_messages.append(error_message)

    if data['image'] == '':
        error_message = "Image URL can't be blank"
        error_messages.append(error_message)
    
    if data['text'] == '':
        error_message = "Text can't be blank"
        error_messages.append(error_message)
    
    if len(error_messages) != 0:
        return render(request, 'tweets/post.html', { 'error_messages': error_messages })
        
    posted_tweet = Tweet(name=data['name'], image=data['image'], text=data['text'], pub_date=timezone.now())
    posted_tweet.save()
    return HttpResponseRedirect(reverse('tweets:index'))

def destroy(request, tweet_id):
    return render(request, 'tweets/index.html')