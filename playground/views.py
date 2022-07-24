from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# View functions are request handlers, they receive a request and send a response
# These view functions need to be mapped to a URL so when a request comes from the URL, the function will be called.

def playground_home(request):
    return HttpResponse("This is the playground home!")

def say_hello(request):
    context = {
        'volk': 'Volk',
        'visual': 'Visual'
    }
    return render(request, 'hello.html')
    



