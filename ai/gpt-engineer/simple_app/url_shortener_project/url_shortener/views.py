from django.shortcuts import render, get_object_or_404, redirect
from .models import URL

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = URL(full_url=request.POST['full_url'])
        url.save()
        return render(request, 'index.html', {'url': url})

def redirect_url(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicks += 1
    url.save()
    return redirect(url.full_url)
