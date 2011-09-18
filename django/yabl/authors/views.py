from django.http import HttpResponse
from yabl.authors.models import Author
from django import template
# Create your views here.

def author_list(request):
    tmpl = template.loader.get_template('author_list.html')
    context = template.Context({'authors': Author.objects.all()})
    response = tmpl.render(context)
    return HttpResponse(response)
