# from importlib.metadata import requires
# from tkinter import Y
# from time import process_time_ns
# from unicodedata import name
# from winreg import REG_RESOURCE_REQUIREMENTS_LIST
# import HTTP responce from Django

import traceback  # use to show the complete error message.

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Book

# Create your views here.

def homepage(request): # request -- HTTP request
    """All basic details of application and start buttons given."""

    name = request.POST.get("bname")     # assigning all book name to variable for optimization
    price = request.POST.get("bprice")   # assigning all book price to variable for optimization
    qty = request.POST.get("bqty")       # assigning all book qty to variable for optimization

    if request.method == "POST":
        if not request.POST.get("bid"):
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name, book_price, book_qty)

            # Store data in database by creating object
            Book.objects.create(name= book_name, price= book_price, qty= book_qty)   # create book details in database
            return redirect("new_book_entry")      # Redirect to the new book entry page
        else:
            bid = request.POST.get("bid")
            try:       
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as err_msg:
                price(err_msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()
            return redirect("show_all_books")   # Redirect to the show all books page
         
    elif request.method == "GET":
        return render(request, template_name="home.html")

def new_book_entry(request):
    """Enter the new book deails to store in database."""
    return render(request, template_name="new_book_entry1.html")  # Redirect to the new book entry page

def show_all_books(request):
    """ This shows the all books available in database."""
    all_books = Book.objects.all()                                 # Gives all book detials
    data = {"books": all_books}
    return render(request, template_name="show_books.html", context=data)   
    # "template_name= " is optional, {"books": all_books} -- Context

def edit_data(request, id):
    """Book details like name, price & qty edit."""
    book = Book.objects.get(id=id)                      # Gives all book detials for required ID
    return render(request, template_name="new_book_entry1.html", context={"single_book":book})

def delete_data(request, id):
    """Delete the single data by provided button."""

    # print(request.method)
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            # print(err_msg)
            traceback.print_exc()
            return HttpResponse(f"Book Does not exist for ID:- {id}")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} Not allowed. Only POST menthod is allowed")

def buy_book(request):
    """Book buy options and book deatils are given"""

    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request, template_name="buy_book.html", context=data)

def address_email(request):
    """Redirect to the book delivery details"""

    return render(request, template_name="address&email.html")

def delete_all(request):
    """Delete all book from database by one button."""

    delete_data = Book.objects.all()
    delete_data.delete() 
    return redirect("show_all_books")

def proceed_to_buy(request):
    """By one submit redirect to the next page."""

    return redirect("address_email")
 
def non_active_book(request):
    """Give the list of non active books."""

    non_active_data = Book.inactive_objects.all()
    data = {"inactive_book": non_active_data}
    return render(request, template_name="non_active_book.html", context=data)

def soft_delete_book(request, id):
    """Inactive the active book in database and stored in database."""

    if request.method == "POST":
        book = Book.active_objects.get(id=id)
        book.is_active = "N"
        book.save()
        return redirect("show_all_books")

def restore_book(request, id):
    """Activate the inactive book and stored in database."""

    if request.method == "POST":
        all_book_data = Book.inactive_objects.get(id=id)
        all_book_data.is_active == "Y"
        all_book_data.save()
    
    all_data = Book.inactive_objects.all()
    data = {"inactive_book": all_data}
    return render(request, template_name="non_active_book.html", context= data)





 
