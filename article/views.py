from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block
from article.models import Article 

def article_list(request,block_id):
    block_id=int(block_id)
    blockss=Block.objects.get(id=block_id)
    articles_objs=Article.objects.filter(block=block_id,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":articles_objs,"b":blockss})
