from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306256356',
        'name': 'H',
        'class': 'KKI'
    }

    return render(request, "main.html", context)
