import os.path
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Work
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import BookForm

def home_page(request):
    articles = Work.objects.all().order_by('slug')
    return render(request,'home.html', {'articles':articles})



def upload(request):
    context = {}
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request,'upload.html',context)

def book_list(request):
    books = Work.objects.all()
    return render(request,"book_list.html",{'books':books})

def upload_book(request):
    if request.method =="POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'upload_book.html',{'form':form})
    form = BookForm()
    return render(request,"upload_book.html",{'form':form})


def contact(request):
    return render(request,'contact.html')



def article_detail(request,slug):
    # return HttpResponse(slug)
    article = Work.objects.get(slug=slug)
    return render(request, "page_of_work.html", {"article": article})
