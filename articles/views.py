from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import ArticleForm, CommentForm
from .models import Article, Comment, Hashtag
from .serializers import CommentSerializer, ArticleSerializer, HashtagSerializer
import json

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    # ori_hashtags = json.dumps(HashtagSerializer(Hashtag.objects.all(), many=True).data)
    # vue_articles = json.dumps(ArticleSerializer(articles, many=True).data)
    # context = {'articles':articles,}
    return render(request, 'articles/index.html')

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save()
            for word in article.content.split(): 
                if word.startswith('#'): 
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag) 
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form':form, }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments_json = json.dumps(CommentSerializer(article.comment_set.all(), many=True).data)
    context = {'article':article, 'comments_json':comments_json}
    return render(request, 'articles/detail.html', context)

def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():            
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)        
    context = {'form':form,}
    return render(request, 'articles/form.html', context)

@api_view(['POST'])
def comment_create(request, article_pk):
    if request.is_ajax():
        form = CommentForm(request.data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
            comment = json.dumps(CommentSerializer(comment).data)
            return JsonResponse(comment, status=201, safe=False)
        else:
            return JsonResponse({'message': 'fail'}, status=202)
    else:
        return HttpResponseBadRequest(401)
        
@require_POST
def comment_delete(request, comment_pk):
    if request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return JsonResponse({"message": "삭제되었습니다."}, status=204)
    return HttpResponseBadRequest(401)
    
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag':hashtag, 'articles':articles,}
    return render(request, 'articles/hashtag.html', context)

def hashtag_list(request):
    hashtags = json.dumps(HashtagSerializer(Hashtag.objects.all(), many=True).data)
    articles = json.dumps(ArticleSerializer(Article.objects.all(), many=True).data)
    context = {'hashtags':hashtags, 'articles':articles,}
    return JsonResponse(context, status=200)
