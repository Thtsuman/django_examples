from django.shortcuts import render
from django.views.generic import (View,TemplateView, ListView,
                                  DetailView, UpdateView, CreateView,
                                  DeleteView)
from basic_app import models
from django.urls import reverse_lazy
# Create your views here.

# class based views
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    # context_object_name = 'school'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')



# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based views")

# function based views
# def index(request):
#     return render(request, 'index.html')
