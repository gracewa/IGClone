from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Photo, Profile
from allauth.account.views import LoginView
from .forms import ProfileForm, ImageUploadForm, PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    userid = request.user.id
    g = get_object_or_404(User, pk=userid)
    i = g.pk

    context = {
        'photos': Photo.objects.all(),
        'profile': get_object_or_404(Profile, pk=i)
    }

    return render(request, 'gallery.html', context)

def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photo_detail.html', context)

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        g = get_object_or_404(User, username=search_term)
        i = g.pk
        profile = get_object_or_404(Profile, pk=i)

        searched_photos = profile.photo_set.all()

        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't entered a search term"
        return render(request, 'search.html',{"message":message})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'successfully uploaded')
            return redirect('core:index')
    else:
        form = ProfileForm()
        return render(request, 'profile.html', {'form': form, 'messages': messages})



def image_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'successfully uploaded')
            return redirect('core:index')
    else:
        form = PhotoForm()
    return render(request, 'photo_upload.html', {'form': form, 'messages': messages})


def success(request):
    return HttpResponse('successfully uploaded')