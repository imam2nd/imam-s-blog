from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.is_valid()
        if form.is_valid():
            form.save()
            user = form.save()

            login(request, user)
            return HttpResponseRedirect(reverse('article_list'))

    else:
        form=UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('article_list'))

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):

    if request.method=='POST':
        logout(request)
        return HttpResponseRedirect(reverse('article_list'))
