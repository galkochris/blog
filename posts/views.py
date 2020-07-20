from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from datetime import datetime





from posts.models import Post, Comment
from posts.forms import PostForm



class PostListView(ListView):
    """ Renders a list of all posts. """
    model = Post

    def get(self, request):
        """ GET a list of Posts. """
        posts = self.get_queryset().all()
        return render(request, 'list.html', {
          'posts': posts
        })

class CommentListView(ListView):
    """ Renders a list of all events. """
    model = Comment

    def get(self, request):
        """ GET a list of events. """
        event = self.get_queryset().all()
        return render(request, 'comment.html', {
          'event': event
        })

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    
    def get_context_data(self, **kwargs):
        """ Returns a specific post page by pk. """
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context

    def post(self, request, pk):
      form = PostForm(request.POST)

      if form.is_valid():
        post = form.save(commit=False)
        post.post = self.get_queryset().get(pk)
        post.title  = request.POST['title']
        post.post = request.POST['post']
        post.image = request.POST['image']
        post.modified = datetime.now()
        post.Author = request.user
        post.save()
        return HttpResponseRedirect(
          reverse('posts-details-page', args=[pk]))
      return render(request, 'post.html', {'form': form})

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')


    def get(self, request):
        context = {
        'form': PostForm()
        }
        return render(request, 'create.html', context)

    def post(self, request, *args):
        form = PostForm(request.POST)
        
        if form.is_valid:
            post = form.save(commit=False)
            post.Author = request.user
            post.save()
            return HttpResponseRedirect(
                reverse('posts-details-page', args=[post.id]))
        #else
        return render(request, 'create.html', { 'form':form })
