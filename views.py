from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block

def index(request):
    block_infos=Block.objects.all().order_by("id")
   # Rplace by DB***************************************************************# 
   # block_infos=[{"name":"运维专区","desc":"运维学习讨论区","manager":"admin"},#
   #         {"name":"Django专区","desc":"Django学习讨论区","manager":"admin"}, #
   #         {"name":"部落建设","desc":"部落建设事宜","manager":"admin"}]       #
   #****************************************************************************#
    return render(request,"index.html",{"blocks":block_infos})
