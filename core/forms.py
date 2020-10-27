from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Profile, Photo


class ProfileForm(forms.Form):
    bio = forms.CharField(label='Update Bio', max_length=500)

class ImageUploadForm(forms.ModelForm):
    image = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'images'
       }
    )
    class Meta:
        model = Profile
        fields = ('image',)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image']