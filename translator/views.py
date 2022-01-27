from django.shortcuts import render

# Create your views here.

#request param gets url passed by url
def translator_view(request):
    return render(request, 'translator.html')