from django.contrib import admin
from posts.models import Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created')
    search_fields = ('name', 'body')

class PostAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'post', 'author', 'image')


admin.site.register(Post, PostAdmin)