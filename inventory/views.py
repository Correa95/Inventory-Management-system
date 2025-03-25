from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category
from inventory_management.settings import LOW_QUANTITY
from django.contrib import messages
# Create your views here.
class Index(TemplateView):
    template_name = "inventory/index.html"


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.filter(user = self.request.user.id).order_by("id")

        low_inventory = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        )
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                # show a message
            else:
                # show a message


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

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    
class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = "inventory/addItemForm.html"
    success_url = reverse_lazy("dashboard")

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = "inventory/deleteItem.html"
    success_url = reverse_lazy("dashboard")
    context_object_name = "item"
    
        
    
    