from django.urls import path

from . import views

urlpatterns = [
   
    path('home/', views.homepage ,name='homepage'),
    path('index/', views.index ,name='index'),
    path('login/', views.login ,name='login'),
   
    #show all books
    path('showbooks/', views.showbooks , name='showbooks'),
    
    #show category
    path('showcategory/', views.books_Category , name='showcategory'),
    
    #show books by using category id
    path('show-books-by-category/<books_id>', views.showbooks_byCat , name='show-books-by-category'),
   
    #add a new book by using  category id
    path('addnewbook/<books_id>',views.addbooks,name='addnewbook'),
   
    #delete book by using its id
    path('deletebook/<id>',views.deletebook,name='deletebook'),

    #edit book by using its id
    path('editbook/<id>',views.editbook,name='editbook'),

    #edit book by using its id
    path('deleteCategory/<id>',views.deleteCategory,name='deleteCategory'),

    #show all persons in db 
    path('showstudents/',views.showstudents,name='showstudents'),

    #add a new personborrowit
    path('addnewperson/',views.addnewperson,name='addnewperson'),

    #add a new person
    path('deleteperson/<id>',views.deleteperson,name='deleteperson'),

    #edit a new person
    path('editperson/<id>',views.editperson,name='editperson'),

    #borrrowbooks
    path('borrowbook/<id>',views.borrowbook,name='borrowbook'),

    #borrrowbooks
    path('borrowit/<book_id><person_id>',views.borrowit,name='borrowit'),

    #borrrowbooks
    path('showborrowers/', views.showborrowers ,name='showborrowers'),

    #returnbook
    path('returnbooks/<id>', views.returnbooks ,name='returnbooks'),

    #returnbook
    path('showreturners/', views.showreturners ,name='showreturners'),



    
   
]
