from django.shortcuts import render
from . import models
def home(request):
    articles= models.articles.objects.filter(status="p").order_by('-updated')
    args={'articles':articles}
    return render(request,'articles/home.html',args)

#nepton,nepton,nepton,...

def ar_list(request):
    articles= models.articles.objects.filter(status="p").order_by('-updated')
    args={'articles':articles}
    return render(request,'articles/ar_list.html',args)

#nepton,nepton,nepton,...

def page(request, slug):
    articles= models.articles.objects.get(slug=slug)
    args={'articles':articles}
    return render(request,'articles/page.html',args)


def post(request, slug):
    articles= models.articles.objects.get(slug=slug)
    args={'articles':articles}
    return render(request,'articles/post.html',args)

def about(request):
    return render(request,'articles/about.html')
