from django.shortcuts import redirect, render
from .models import Content
from .forms import ContactForms

def home(request):
    portfolio_items = Content.objects.filter(category__slug='article', isActive=True)
    for item in portfolio_items:
        if item.content_type == 'video':
            item.type = 'video'
            item.poster = item.extraData.get('poster')
            item.video_src = item.extraData.get('video_src')
        elif item.content_type == 'slider':
            item.type = 'slider'
            item.images = item.extraData.get('images', [])
        elif item.content_type == 'image':
            item.type = 'image'
    return render(request, 'pages/home.html', {'portfolio_items': portfolio_items})

def about(request):
    feature_items = Content.objects.filter(category__slug='feature', isActive=True)
    return render(request, 'pages/about.html', {'feature_items': feature_items})

def project(request):
    gallery_items = Content.objects.filter(category__slug='gallery', isActive=True)
    return render(request, 'pages/project.html', {'gallery_items': gallery_items})

def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = ContactForms() 
    return render(request, 'pages/contact.html', {'form': form})
