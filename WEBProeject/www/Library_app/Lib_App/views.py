from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

from .models import *
from Lib_App import models
from .forms import *
from datetime import date


# .FORMS REFERS TO THE FORMS.PY IN CURRENT DIRECTORY AND * USED FOR IMPORTING EVERYTHING

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# HOME PAGE
def index(request):
    return render(request,'index.html')




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'homepage.html')


#show all books
def showbooks(request):
    books=models.books.objects.all()
    books_types=models.books_types.objects.all()
    context={'books':books,'books_types':books_types}
    return render(request,'books.html',context)


def showbooks_byCat(request,books_id):
    books=models.books.objects.filter(books_id = books_id)
    context={'books':books}
    return render(request,'books-byCat.html',context)

def books_Category(request):
    books_types=models.books_types.objects.all()
    if request.method == "POST":
        books_types=models.books_types()
        form = booksTypeForm(request.POST)
        if form.is_valid():
            books_types.book_type_name = form.cleaned_data['book_type_name']
            books_types.save()
            return HttpResponseRedirect('/lib/showcategory/')

    else:
        form = booksTypeForm()
        books_types=models.books_types.objects.all()

    


    context={'books_types':books_types,'form':form}
    return render(request,'Category.html',context)




#add new book by using id of category
@login_required
def addbooks(request,books_id):

    book = models.books()
    bookid=models.books_types.objects.get( id = books_id)
    if request.method == "POST":
        form = booksForm(request.POST)
        if form.is_valid():
            #book = form.save(commit = False)
            book.books_id=bookid
            book.books_name = form.cleaned_data['books_name']
            book.author_name = form.cleaned_data['author_name']
            book.publisher_name=form.cleaned_data['publisher_name']
            book.books_numbers=form.cleaned_data['books_numbers']
            book.books_date=form.cleaned_data['books_date']
            book.save()
            return HttpResponseRedirect('/lib/showcategory/')
            #return HttpResponse('Película creada correctamente!✔️')

    else:
        form = booksForm()

    return render(request,'addnewbook.html',{'books_id':books_id,'form':form})


@login_required
def deletebook(request, id):
    book= models.books.objects.get(id=id)
    book.delete()
    return redirect('/lib/showbooks/')

@login_required
def editbook(request,id):

    book = models.books.objects.get(id = id)
    if request.method == "POST":
        form = booksForm(request.POST)
        if form.is_valid():
            #book = form.save(commit = False)
        
            book.books_name = form.cleaned_data['books_name']
            book.author_name = form.cleaned_data['author_name']
            book.publisher_name=form.cleaned_data['publisher_name']
            book.books_numbers=form.cleaned_data['books_numbers']
            book.books_date=form.cleaned_data['books_date']
            book.save()
            return HttpResponseRedirect('/lib/showcategory/')
            

    else:
        form = booksForm(initial= {'books_name': book.books_name,'author_name':book.author_name,'publisher_name':book.publisher_name,
    'books_numbers':book.books_numbers,'books_date':book.books_date
    })

    return render(request, 'editbook.html',{'form': form, 'book': book})

@login_required
def deleteCategory(request, id):
    book= models.books_types.objects.get(id=id)
    book.delete()
    return redirect('/lib/showcategory/')




#show all persons
@login_required
def showstudents(request):
    persons=models.persons.objects.all()
    context={'persons':persons}
    return render(request,'showstudents.html',context)


@login_required
def addnewperson(request):
    person = models.persons()
    if request.method == "POST":
        form = personForm(request.POST)
        if form.is_valid():
            person.person_id = form.cleaned_data['person_id']
            person.person_type = form.cleaned_data['person_type']
            person.person_name=form.cleaned_data['person_name']
            person.person_due=form.cleaned_data['person_due']
          
            person.save()
            return HttpResponseRedirect('/lib/showstudents/')
            

    else:
        form = personForm()

    return render(request,'addstudent.html',{'form':form})


@login_required
def deleteperson(request, id):
    person= models.persons.objects.get(id=id)
    person.delete()
    return redirect('/lib/showstudents/')


@login_required
def editperson(request,id):

    person = models.persons.objects.get(id = id)
    if request.method == "POST":
        form = personForm(request.POST)
        if form.is_valid():
            #book = form.save(commit = False)
        
            person.person_id = form.cleaned_data['person_id']
            person.person_type = form.cleaned_data['person_type']
            person.person_name=form.cleaned_data['person_name']
            person.person_due=form.cleaned_data['person_due']
          
            person.save()
            return HttpResponseRedirect('/lib/showstudents/')
            

    else:
        form = personForm(initial= {'person_id': person.person_id,'person_type':person.person_type,'person_name':person.person_name,
    'person_due':person.person_due})

    return render(request, 'editperson.html',{'form': form})


def borrowbook(request,id):
    book=models.books.objects.get(id=id)
    persons=models.persons.objects.all()
    context={
        'book':book,
        'persons':persons
    }



    return render(request, 'borrowbook.html',context)


def borrowit(request,book_id,person_id):
    today=date.today()

    

    person=models.persons.objects.get(id=person_id)
    book=models.books.objects.get(books_name=book_id)

    if(book.books_numbers>0):
        borrowbook=models.borrowerbook()
        borrowbook.person_id=person.person_id
        borrowbook.person_name=person.person_name
        borrowbook.book_name=book_id
        borrowbook.issue_date = today
        borrowbook.save()
        book.books_numbers=book.books_numbers - 1
        book.save()
        return redirect('/lib/showcategory/')
    else:
        return(HttpResponse("There is no Copies of '"+book_id+"'now,"))

def showborrowers (request):
    Borrowers=models.borrowerbook.objects.all()
    
    
    return render(request, 'showborrowers.html',{'Borrowers':Borrowers})
    
def returnbooks(request, id ):
    today=date.today()
    Borrowers=models.borrowerbook.objects.get(id=id)
    
    book=models.books.objects.get(books_name=Borrowers.book_name)

   
    returnbook=models.returnbook()
    returnbook.person_id=Borrowers.person_id
    returnbook.person_name=Borrowers.person_name
    returnbook.book_name=Borrowers.book_name
    returnbook.return_date = today
    returnbook.save()
    book.books_numbers=book.books_numbers + 1
    book.save()
    Borrowers.delete()

    return redirect('/lib/showborrowers/')
   

def showreturners (request):
    returners=models.returnbook.objects.all()
    
    
    return render(request, 'showreturners.html',{'returners':returners})

    

   
    
    
    







