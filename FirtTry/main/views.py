from django.shortcuts import render

def index(request):
    data = {
        'title': 'Обо мне',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, "main/index.html", data)

def portfolio(request):
    return render(request, "main/portfolio.html")

def contacts(request):
    return render(request, "main/contacts.html")