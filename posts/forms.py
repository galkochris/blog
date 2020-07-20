from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    """ Render and process a form based on the Post model. """
    class Meta:
        model = Post
        fields = ['title', 'image', 'post']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'comment']