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
    posted_tweet = Tweet(name=data['name'], image=data['image'], text=data['text'], pub_date=timezone.now())
    posted_tweet.save()
    return HttpResponseRedirect(reverse('tweets:index'))