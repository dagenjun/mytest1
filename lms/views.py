#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import Context
from django.shortcuts import render_to_response
from models import *


	
def add_book(request):
	if request.POST:
		post = request.POST
		newbook=book(
			isbn = post["isbn"],
			title = post["title"],
    		author = author.objects.get_or_create(name = post["name"])[0],
    		publisher = post["publisher"],
    		publishdate = post["publishdate"],
    		price = post["price"],
            )
		newbook.save()

		return HttpResponseRedirect("/")  
	return render_to_response("add_book.html")


def update_book(request, uisbn = 1):
	if request.POST:
		post = request.POST
		a = post['isbn']
		newbook = book(
			isbn = post['isbn'],
			title = post["title"],
    		author = author.objects.get_or_create(name = post["name"])[0],
    		publisher = post["publisher"],
    		publishdate = post["publishdate"],
    		price = post["price"],
    		)
		newbook.save()
		return HttpResponseRedirect("/")
	else:
		content = {"isbn": uisbn}
		return render_to_response("update_book.html", content)	
	return render_to_response("update_book.html")
			


def delete_book(request):
	if request.POST:
 		post = request.POST
		a = post["isbn"]
		book.objects.get(isbn = a).delete()
		return render_to_response("all_book.html")	
	else:
		books = book.objects.all()
		content = {"book_list": books}
		return render_to_response("all_book.html", content)	


def title_book(request):
	a = request.GET['title']
	listbook=book.objects.filter(title = a)
	content = {"book":listbook}         
	return render_to_response("title_book.html",content)


def index(request):
	return render_to_response("add_book.html")

'''
def title_book(request):
	return render_to_response("title_book.html")

def author_book(request):
 	return render_to_response("author_book.html")
'''