from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView , FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasklist')


class RegisterPage(FormView):
    template_name = 'base/Register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasklist') 

    def form_vaild(self,form):
        user= form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_vaild(form)
    
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context ['search_input']=search_input
        return context
     
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' 

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']  
    success_url = reverse_lazy('tasklist') 
    template_name = 'base/task_form.html'

    def form_vaild(self,form):
        form.instance.user=self.request.user
        return super(TaskCreateView,self).form_vaild(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']  
    success_url = reverse_lazy('tasklist') 
    template_name = 'base/task_form.html'

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasklist')