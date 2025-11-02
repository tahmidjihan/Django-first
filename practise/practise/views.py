from django.http import HttpResponse

def Home(request):
    return HttpResponse("This is my home page")
def About(request):
    return HttpResponse("This is my About page")
def Blogs(request):
    return HttpResponse("This is my blogs page")