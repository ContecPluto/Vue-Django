from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles':articles, }
    return render(request, 'articles/index.html', context)

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {'form':form, }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    comments = article.comment_set.all()
    context = {'article':article, 'form':form, 'comments':comments, }
    return render(request, 'articles/detail.html', context)

@require_POST
def comment_create(request, article_pk):
    if request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
        # return redirect('articles:detail', article_pk)
        comments = Comment.objects.all()
        context  = {'commetns':comments}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest
        

        
        
@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    
