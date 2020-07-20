from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'post', 'Author', 'image')


admin.site.register(Post, PostAdmin)