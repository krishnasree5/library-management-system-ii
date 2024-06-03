from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):

    isbn = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name= 'books', on_delete=models.CASCADE)
    publisher = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book-images', blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
