from django.http import HttpResponse
def movies(request):
    return HttpResponse("Hello Django!")
def homepage(req):
    return HttpResponse("Home Page")
