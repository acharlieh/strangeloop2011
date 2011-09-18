from django.http import HttpResponse
from yabl.authors.models import Author
# Create your views here.

def author_list(request):
    response = '<ul>'
    for author in Author.objects.all():
        response += '<li>%s</li>' % author
    response += '</ul>'
    return HttpResponse(response)
