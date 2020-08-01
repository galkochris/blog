from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from datetime import datetime





from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm



class PostListView(ListView):
    """ Renders a list of all posts. """
    model = Post

    def get(self, request):
        """ GET a list of Posts. """
        posts = self.get_queryset().all()
        return render(request, 'list.html', {
          'posts': posts
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
    
    def comment(self, request, pk):
      post = get_object_or_404(Post, pk=pk)
      form = CommentForm(request.POST)
      if request.method == "POST":
        if form.is_valid():
          comment = form.save(commit=False)
          comment.post = post
          comment.save()
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
            post.author = request.user
            post.save()
            return HttpResponseRedirect(
                reverse('posts-details-page', args=[post.id]))
        #else
        return render(request, 'create.html', { 'form':form })

def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(
                reverse('posts-details-page', args=[post.pk]))
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})