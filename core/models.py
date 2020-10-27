from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    bio = models.CharField(max_length=500)
    image = CloudinaryField('image', blank=True, null=True)
    followers = models.IntegerField(default=0)
    user = models.ForeignKey(User, blank=True,
                             null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    @classmethod
    def search_by_user(cls, username):
        profile = cls.objects.filter(user__username=username)
        return profile

class Photo(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='noimage.png')
    description = models.CharField(max_length=500, default='no description')
    user = models.ForeignKey(User, blank=True,
                                 null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, blank=True,
        null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_user(cls, search_term):
        photos = cls.objects.filter(user__username=search_term)
        return photos

