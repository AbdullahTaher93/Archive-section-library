from django.db import models



#create books category table
class books_types(models.Model):
    book_type_name=models.CharField(max_length=15)
    def __str__(self):
        return self.book_type_name
    
    

#create table of  books details 
class books(models.Model):
    books_id=models.ForeignKey(books_types,on_delete=models.CASCADE)
    books_name=models.CharField(max_length=25)
    author_name=models.CharField(max_length=25)
    publisher_name=models.CharField(max_length=15)
    books_numbers=models.IntegerField(default=1)
    books_date=models.DateField()
    def __str__(self):
        return self.books_name

class persons(models.Model):
    
    person_id=models.CharField(max_length=25)
    person_type=models.CharField(max_length=25,choices=(("Professor","Professor"),("Student","Student"),("Employ","Employ")))
    person_name=models.CharField(max_length=25)
    person_due=models.IntegerField(max_length=1)
    def __str__(self):
        return self.person_name

class borrowerbook(models.Model):
    person_id=models.CharField(max_length=25)
    person_name=models.CharField(max_length=25)
    book_name=models.CharField(max_length=25)
    issue_date = models.CharField(max_length=25)
    
    def __str__(self):
        return self.person_name

class returnbook(models.Model):
    person_id=models.CharField(max_length=25)
    person_name=models.CharField(max_length=25)
    book_name=models.CharField(max_length=25)
    return_date = models.CharField(max_length=25)
    
    def __str__(self):
        return self.person_name






    

