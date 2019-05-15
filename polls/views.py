from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're a the polls index.")
