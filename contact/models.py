from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """Class model """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """Class models contacts"""
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """Class models page about us"""
    text = RichTextField()
    mini_text = RichTextField()

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]


class ImageAbout(models.Model):
    """Class models image page about us"""
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")
    alt = models.CharField(max_length=100)


class Social(models.Model):
    """Class models social network about us"""
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()




