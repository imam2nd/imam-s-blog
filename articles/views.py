from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from .models  import Article
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles':articles})
def khit(request):
    return render(request, 'articles/khit.html')

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse('article_list'))
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
