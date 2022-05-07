from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Profile

# Create your views here.
class Profile_List(ListView):
    pass

class Profile_Details(DetailView, ):
    pass

class Profile_UpdateView(UpdateView):
    pass

class Profile_DeleteView(DeleteView):
    pass
