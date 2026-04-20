from django.contrib import admin
from .models import Post, Category, Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "text", "created_at"]
    list_filter = ["user", "created_at"]
    search_fields = ["text",  "user__username"]
    ordering = ["-created_at"]

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Like)