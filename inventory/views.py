from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category

# Create your views here.
class Index(TemplateView):
    template_name = "inventory/index.html"


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.filter(user = self.request.user.id).order_by("id")
        return render(request, "inventory/dashboard.html", {"items":items})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "inventory/signup.html", {"form":form})


    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password1"]
            )
            login(request, user)
            return redirect("index")
        return render(request, "inventory/signup.html" , {"form": form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = "inventory/addItemForm.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    
class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = "inventory/item_form.html"
    success_url = reverse_lazy("dashboard")
        
    
    