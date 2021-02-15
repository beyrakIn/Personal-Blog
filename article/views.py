from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from .models import Article, Social, Message, AboutMe

# Create your views here.
articles = Article.objects.all()
social = Social.objects.first()
about_me = AboutMe.objects.first()


def index(request):
    return render(request, 'index.html', {"articles": articles, "social": social})


def single(request, pk):
    article = articles.filter(id=pk).first()
    return render(request, 'single.html', {"article": article, "social": social})


def about(request):
    return render(request, 'about.html', {"social": social, "about": about_me})


def work(request):
    return render(request, 'work.html', {"social": social})


def contact(request):
    return render(request, 'contact.html', {"social": social})


@requires_csrf_token
def upload_image_view(request):
    files = request.FILES['image']
    fs = FileSystemStorage()
    filename = str(files).split('.')[0]
    file_ = fs.save(filename, files)
    file_url = fs.url(file_)
    return JsonResponse({'success': 1, 'file': {'url': file_url}})


@requires_csrf_token
def upload_file_view(request):
    files = request.FILES['file']
    fs = FileSystemStorage()
    filename, ext = str(files).split('.')
    file_ = fs.save(filename, files)
    file_url = fs.url(file_)
    return JsonResponse({'success': 1,
                         'file': {'url': file_url, "size": fs.size(filename), "name": str(files), "extension": ext}}
                        )
