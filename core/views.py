from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Photo, Profile
from allauth.account.views import LoginView
from .forms import ProfileForm, ImageUploadForm, PhotoForm
from django.contrib.auth.decorators import login_required



def index(request):
    locations = ['Nairobi', 'Mombasa', 'Online', 'Abroad']
    context = {
        'photos': Photo.objects.all(),
        'locations':locations
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
        searched_photos = Photo.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't entered a search term"
        return render(request, 'search.html',{"message":message})

@login_required
def update_profile(request):
    user = request.user.username

    profile = Profile.search_by_user(user)
    if request.method == "POST":
        bioform = ProfileForm(request.POST)
        if bioform.is_valid():
            for i in profile:
                i.bio = bioform.cleaned_data['bio']
                i.save_profile()
    updated_profile = Profile.search_by_user(user)
    form = ImageUploadForm()
    bioform = ProfileForm()
    return render(request, 'profile.html', {'form': form, 'bioform':bioform, 'updated_profile':updated_profile})


def image_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('core:success')
    else:
        form = PhotoForm()
    return render(request, 'photo_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')