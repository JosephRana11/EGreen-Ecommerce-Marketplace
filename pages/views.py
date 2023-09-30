from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from product.models import Product
from django.contrib.auth import authenticate , login , logout

def home_view(request):
  obj = Product.objects.filter(is_approved=True)
  context = {
    'obj':obj
  }
  return render(request , 'home.html' , context)

def login_view(request):
  if request.method == 'POST':
    print(request.POST)
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    user = authenticate(request , username = username , password = password)
    if user is not None:
      login(request , user)
      return redirect('home')
    else:
      return redirect('login')
  else:
   return render(request , 'login.html')

def logout_view(request):
  logout(request)
  return redirect('home')

def about_view(request):
  return render(request , 'about.html')

def contact_view(request):
  return render(request , 'contact.html')