from django.shortcuts import render, redirect, HttpResponse

def index(request):
  return HttpResponse('placeholder to later display a list of all blogs')

def root(request):
  return redirect('/blogs')

def new(request):
  return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
  return redirect('/')

def show(request, num):
  context = {
    'number': num,
  }
  return render(request, 'index.html', context)

def edit(request, num):
  context = {
    'number': num,
  }
  return render(request, 'edit.html', context)

def destroy(request, num):
  return redirect('/blogs')
# Create your views here.
