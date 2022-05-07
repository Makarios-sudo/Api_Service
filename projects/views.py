from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.

class Tutorials_List(ListView):
    pass

class Tutorial_Details(DetailView, ):
    pass

class Tutorial_Update_view(UpdateView):
    pass

class Tutorial_Delete_view(DeleteView):
    pass
