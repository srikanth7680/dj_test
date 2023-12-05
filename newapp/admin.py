from django.contrib import admin
from newapp.models import Books,Library_patron, Book_Borrowing
# Register your models here.
admin.site.register(Books)
admin.site.register(Library_patron)
admin.site.register(Book_Borrowing)