from django.http import HttpResponse
from yabl.authors.models import Author
from django.shortcuts import render
# Create your views here.

def author_list(request):
    return render(request, 'author_list.html',{'authors': Author.objects.all()});

