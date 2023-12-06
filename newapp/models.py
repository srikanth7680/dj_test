from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    ISBN = models.IntegerField()
    availability_status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Library_patron(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.IntegerField()
    membership_details = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Book_Borrowing(models.Model):
    book = models.CharField(max_length=100)
    patron = models.CharField(max_length=100)
    borrowing_date = models.DateField()
    return_date = models.DateTimeField()
    def __str__(self):
        return self.book
