from django.shortcuts import render
from datetime import datetime
from .forms import FilterForm
from django.http import HttpResponse
from .models import subcategory_choices, about, director, img_slider, staff, faq, feedback, guideline, announcement, sop, certificate, event, project, gallery

today = datetime.today()
# Create your views here.
def index(request):
    introduction = about.objects.all()
    faq1 = faq.objects.all()
    direct = director.objects.all()
    announce = announcement.objects.all()
    eve = event.objects.filter(eventdate__gte=today)
    photos = gallery.objects.all()
    guide = guideline.objects.all()
    slider = img_slider.objects.all()
    context = { 'introduction': introduction,'faq1': faq1,'announce': announce, 'eve': eve, 'photos': photos,   'guide': guide,'direct':direct,'slider': slider }
    return render(request, 'index.html', context)

def intro(request):
    introduction = about.objects.all()
    context = { 'introduction': introduction }
    return render(request, 'about.html', context)

def faqq(request):
    faq1 = faq.objects.all()
    context = { 'faq1': faq1 }
    return render(request, 'faq.html', context)

def galleryphotos(request):
    photos = gallery.objects.all()
    context = { 'photos': photos }
    return render(request, 'gallery.html', context)

def members(request):
    member = staff.objects.all()
    direct = director.objects.all()
    context = { 'member': member, 'direct' : direct }
    return render(request, 'staff.html', context)

def cert(request):
    certf = certificate.objects.all()
    context = { 'certf': certf }
    return render(request, 'certificates.html', context)

def sops(request):
    sopp = sop.objects.all()
    context = { 'sopp': sopp }
    return render(request, 'sops.html', context)

def pastevents(request):
    today = datetime.today()
    even = event.objects.filter(eventdate__lt=today)
    context = { 'even': even }
    return render(request, 'pastevents.html', context)

def upevents(request):
    today = datetime.today()
    eve = event.objects.filter(eventdate__gte=today)
    context = { 'eve': eve }
    return render(request, 'upevents.html', context)

def guidelines(request):
    guide = guideline.objects.all()
    context = { 'guide': guide }
    return render(request, 'guidelines.html', context)

def announcements(request):
    announce = announcement.objects.all()
    context = { 'announce': announce }
    return render(request, 'announcements.html', context)

def projectsynopsis(request):
    proj = project.objects.filter(category='synopsis')
    context = {'proj': proj, 'subc':subcategory_choices }
    return render(request, 'synopsis.html', context)

def projectnonsynopsis(request):
    proj = project.objects.filter(category='nonsynopsis')
    context = {'subc':subcategory_choices,'proj':proj }
    return render(request, 'nonsynopsis.html', context)

def projectpost(request, id):
    post = project.objects.filter(id = id)[0]
    context = { 'post': post }
    return render(request, 'projectpost.html', context)

def contacts(request):
    thanks = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        feedback1 = feedback(name=name, email=email, subject=subject, message=message)
        feedback1.save()
        thanks = True
    return render(request, 'contact.html', {'thanks': thanks})
