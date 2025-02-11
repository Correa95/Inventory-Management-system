from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm

# Create your views here.
class Index(TemplateView):
    template_name = "inventory/index.html"

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "inventory/signup.html", {"form":form})


    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data.get("username"),
                password = form.cleaned_data.get("password1")
            )
            login(request, user)
            return redirect("index")
        return render(request, "inventory/signup.html" , {"form": form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')