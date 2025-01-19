from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.fullname


class Editor(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=100, blank=True)
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    ISBN = models.CharField(max_length=100, blank=True)
    pub_year = models.PositiveSmallIntegerField(blank=True)
    type_cover = {
        ('Ha', 'Hardcover'),
        ('So', 'Softcover'),} 
    cover = models.CharField(max_length=2, choices=type_cover, default='So')
    states = {
        ('Ne', 'New'),
        ('Ex', 'Used Excellent'),
        ('Gd', 'Used Good'),
        ('Fr', 'Used Fair'),
        ('Po', 'Used Poor')}
    state = models.CharField(max_length=2, choices=states, default='Ex')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    pages = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        authors = ', '.join(author.fullname for author in self.authors.all())
        return f"{self.title} by {authors} editor {self.editor.name}" 