from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406435963',
        'name': 'Jefferson Tirza Liman',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)