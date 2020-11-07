from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import ShortUrl

def index(request):
    urls = ShortUrl.objects.all()
    return render(request, 'index.html', { 'urls' : urls })

def generate(request):
    if request.method == 'POST':
        #generate
        if request.POST['original'] and request.POST['short']:
            #generate based on user input
            print(request.POST['original'])
            print("request.POST['short']")
            original = request.POST['original']
            short = request.POST['short']
            check = ShortUrl.objects.filter(shorturl = short)
            if not check:
                newurl = ShortUrl(
                    url = original,
                    shorturl = short
                )
                newurl.save()
                return redirect('/')
            else:
                messages.error(request, "empty fields")
                return redirect('/')
        elif request.POST['original']:
            #generate random
            pass
        else:
            messages.error(request, "empty fields")
            return redirect('/')
    else:
        return redirect('/')