from django.shortcuts import render


def index(request):
    date = {
        'title': 'Главная страница'
    }
    return render(request,'main/index.html', date)

def about(request):
    date = {
        'title': 'Страница про нас'
    }
    return render(request, 'main/about.html', date)

def inf(request):
    return render(request, 'main/inf.html')
def inf2(request):
    return render(request, 'main/inf2.html')