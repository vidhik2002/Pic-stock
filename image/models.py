from django.db import models

# Create your models here.


class Category(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return self.Title


class Image_Create(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Clicked_by = models.CharField(max_length=50)
    Uploaded_on = models.DateTimeField()
    Image = models.ImageField(upload_to='images')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return ("{}".format(self.Title))
