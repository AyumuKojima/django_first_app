from django.shortcuts import render, get_object_or_404
from django.views import generic
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