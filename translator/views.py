from django.shortcuts import render

# Create your views here.

#request param gets url passed by url
def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = original_text.upper()
        return render(request, 'translator.html', 
        {'output_text':output, 'original_text':original_text})
    else:
        return render(request, 'translator.html')