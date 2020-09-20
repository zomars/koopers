from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Profile
from django.http import JsonResponse
# Create your views here.

def testPanel(request):

  return render(
    request=request,
    template_name='test.html',
    context={}
  )

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'is_admin': request.user.profile.is_admin})
        else:
            return JsonResponse({"message":"Invalidad username or password"})
    return render(
        request=request,
        template_name='login.html',
        context={}
    )

@login_required
def logoutView(request):
  logout(request)
  return redirect('core:login')

def signup(request):

  if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
        data = form.cleaned_data
        name = data['first_name']
        last_name = data['last_name']
        email = data['username']
        password1 = data['password1']
        password2 = data['password2']
        is_admin = data['is_admin']
        user = User.objects.create_user(username=email, email=email, password=password1)
        user.first_name = name
        user.last_name = last_name
        user.save()
        p = Profile(user=user, is_admin=is_admin)
        p.save()

        # messages.success(request, 'Registro exitoso.')
        return redirect('core:login')
      else:
        print(form.errors)
  else:
    form = SignUpForm()
  return render(
    request=request,
    template_name='signup.html',
    context={
      'form': form
    }
  )