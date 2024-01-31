from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, world. You're at the Hello World Page.")
