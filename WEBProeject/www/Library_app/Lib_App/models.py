from django.db import models

class books_types(models.Model):
    book_type_name=models.CharField(max_length=15)
    def __str__(self):
        return self.book_type_name
    

# Create your models here.
class books(models.Model):
    books_id=models.ForeignKey(books_types,on_delete=models.CASCADE)
    books_name=models.CharField(max_length=25)
    author_name=models.CharField(max_length=25)
    publisher_name=models.CharField(max_length=15)
    books_numbers=models.IntegerField(default=1)
    books_date=models.DateTimeField()
    def __str__(self):
        return self.books_name


    

