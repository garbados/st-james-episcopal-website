# Create your views here.
from basic.blog.models import *
from basic.events.models import *
from basic.media.models import *
from django.shortcuts import render
from django.views.generic import list_detail

from forms import ContactForm

def home(request):
    """Front page."""
    c = {}
    image_urls = [
        "http://www.housecatscentral.com/kittens.jpg",
        "http://o.onionstatic.com/images/articles/article/9783/Sidebox-Kitten-Thinks-R_jpg_630x1200_upscale_q85.jpg",
        "http://images2.fanpop.com/images/photos/5800000/happy-kitten-kittens-5890512-1600-1200.jpg",
        "http://myspacenow.com/wp-content/uploads/2011/09/pics-of-kittens-3.jpg",
    ]
    image_alts = [
        "D'aww, look at the kitty!",
        "Such cute kittens!",
        "I want to pet all of them!",
        "Christmas kitty!",
    ]
    images = zip(image_urls,image_alts)
    c['pic'] = {
        "images" : images,
        "height" : 770/2,
        "width" : 770,
    }
    return render(request, 'home.html', c)

def event_list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Event.objects.all(),
        **kwargs)

def contact(request):
    c = dict(contact_form = ContactForm)
    if request.POST:
        # process the form
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
        c['success'] = True
    return render(request, 'contact.html', c)