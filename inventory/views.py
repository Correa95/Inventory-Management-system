from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.
class Index(TemplateView):
    template_name = "inventory/index.html"

class SignUp(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "inventory/sign.html")


    def post(self, request):