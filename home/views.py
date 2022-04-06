from django.shortcuts import render,redirect
from home.forms import BookForm
from home.models import Book
from django.http import HttpResponse
import mysql.connector as sql
fn =''
ln =''
em =''
pwd =''


# Create your views here.

def index(request):
    return render(request,'index.html')

def student(request):
    books = Book.objects.all()
    return render(request,"student.html", {'books':books})
    # return render(request,'student.html')

def signin(request):
    global em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="manojzine8@1435",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value  
            if key=="password":
                pwd=value    

        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'signin.html')
        else:
            # return render(request,"show.html")
             return redirect("/show")

    return render(request,'signin.html')

def signup(request):
    global fn,ln,em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="manojzine8@1435",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value  
            if key=="email":
                em=value  
            if key=="password":
                pwd=value    

        c="insert into users values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()
        return redirect('/signin')

    return render(request,'signup.html')


def book_library(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
                # return render(request,'show.html')
            except:
                pass
    else:
        form=BookForm()                
    return render(request,'book_library.html',{'form':form})


def show(request):
    books = Book.objects.all()
    return render(request,"show.html", {'books':books})

def edit(request, id):
    book = Book.objects.get(id=id)
    return render(request,"edit.html",{'book':book})

def update(request, id):
    book= Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'book':book})

def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/show")

    