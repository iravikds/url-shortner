from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import ShortUrl
import random, string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request, query=None):
    urls = ShortUrl.objects.all()
    if not query or query is None:
        return render(request, 'index.html', { 'urls' : urls })
    else:
        try:
            check_db = ShortUrl.objects.get(shorturl = query)
            check_db.visits = check_db.visits + 1
            check_db.save()
            get_full_url = check_db.url
            return redirect(get_full_url)
        except ShortUrl.DoesNotExist:
            messages.error(request, "does not exists")
            return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def generate_random():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

def generate(request):
    if request.method == 'POST':
        #generate
        if request.POST['original'] and request.POST['short']:
            #generate based on user input
            original = request.POST['original']
            short = request.POST['short']
            check_db = ShortUrl.objects.filter(shorturl = short)
            if not check_db:
                newurl = ShortUrl(
                    url = original,
                    shorturl = short
                )
                newurl.save()
                return redirect('/')
            else:
                messages.error(request, "already exists")
                return redirect('/')
        elif request.POST['original']:
            #generate random
            original = request.POST['original']
            generated = False
            while not generated:
                short = generate_random()
                check_db = ShortUrl.objects.filter(shorturl = short)
                if not check_db:
                    newurl = ShortUrl(
                        url = original,
                        shorturl = short
                    )
                    newurl.save()
                    return redirect('/')
                else:
                    continue
        else:
            messages.error(request, "empty fields")
            return redirect('/')
    else:
        return redirect('/')