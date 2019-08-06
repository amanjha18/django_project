from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print (request.user)
   # return HttpResponse("<h1>Hello world</h1>") #string of html code.
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
   # return HttpResponse("<h1>Contact Page<h1>")
    return render(request, "contact.html",{})
    
def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About Page<h1>")
    my_context={
        "title": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list":[321, 4242, 13132,"aman"],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "about.html",my_context)

def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Social Page</h1>")
    return render(request, "social.html",{})


