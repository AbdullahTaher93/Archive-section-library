from django import forms


class booksForm(forms.Form):
    books_name = forms.CharField(required = True, label = 'Book Name', max_length=200)
    author_name  = forms.CharField(required = True, label = 'Author Name')
    publisher_name = forms.CharField(required = True, label = 'Publisher Name')
    books_numbers = forms.IntegerField(required = True, label = 'Copies number',max_value=3,min_value=0)
    books_date =forms.DateField(initial='2022-03-03')

class booksTypeForm(forms.Form):
    book_type_name= forms.CharField(required = True, label = 'Enter a new Category', max_length=200)


class personForm(forms.Form):
    person_id=forms.CharField(required = True, label = 'Person ID',max_length=25)
    person_type= forms.ChoiceField(choices=(("1","Professor"),("2","Student"),("3","Employ")))
    person_name=forms.CharField(required = True, label = 'Person Name',max_length=25)
    person_due=forms.IntegerField(required = True, label = 'Books Brrowos')


class borrowerbookForm(forms.Form):
    person_id=forms.CharField(required = True, label = 'Person ID',max_length=25)
    person_name=forms.CharField(required = True, label = 'Person Name',max_length=25)
    book_name=forms.CharField(required = True, label = 'Person Name',max_length=25)
    issue_date = forms.DateField(initial='2022-03-03')


class returnbookForm(forms.Form):
    person_id=forms.CharField(required = True, label = 'Person ID',max_length=25)
    person_name=forms.CharField(required = True, label = 'Person Name',max_length=25)
    book_name=forms.CharField(required = True, label = 'Person Name',max_length=25)
    return_date = forms.DateField(initial='2022-03-03')
    

    