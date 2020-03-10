from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {
        'text':'hello world',
        'number':100,
    }
    return render(request, 'qapp/index.html', context=context_dict)

def other(request):
    return render(request, 'qapp/other.html')

def relative(request):
    return render(request, 'qapp/relative_url_templates.html')
