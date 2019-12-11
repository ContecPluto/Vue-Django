from django.contrib import admin
from .models import Article, Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    list_display_links = ('title', )
    # list_editable = ('content', )
    # list_editable 즉시변경가능
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
