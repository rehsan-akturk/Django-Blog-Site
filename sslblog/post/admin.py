from django.contrib import admin
from .models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
     list_display=('post','comment_author','comment_content','comment_date')

admin.site.register(Comment,CommentAdmin)



