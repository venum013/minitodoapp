from django.shortcuts import render,redirect
from .models import ToDo
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class Page(View):
    def get(self,request):
        todos = ToDo.objects.filter(user=request.user)

        return render(request=request,template_name='index.html',context={'todos':todos})

    def post(self,request):
        text = request.POST.get("text")
        ToDo.objects.create(user=request.user,text=text) 
        return redirect("Page") 
    
class New(View):
    def post(self,request,todo_id):
        
        todo = ToDo.objects.get(id=todo_id)
        todo.delete()
        return redirect("Page") 
        
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'