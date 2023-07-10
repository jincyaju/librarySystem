from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,UpdateView,CreateView
from django.urls import reverse_lazy
from libmanage.models import BookModel
from libmanage.forms import BookCreateForm,BookChangeForm


# Create your views here.
class BookCreateView(CreateView):
    model=BookModel
    form_class=BookCreateForm
    template_name='book-add.html'
    success_url=reverse_lazy("book-list")
    

class BookListView(ListView):
    model=BookModel
    template_name='book-list.html'
    context_object_name='books'



class BookDetailView(DetailView):
    model=BookModel
    template_name='book-detail.html'
    context_object_name='book'

class BookEditView(UpdateView):
    model=BookModel
    form_class=BookChangeForm
    template_name='book-edit.html'
    success_url=reverse_lazy("book-list")

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=BookModel.objects.get(id=id)
        BookModel.objects.get(id=id).delete()
        return redirect('book-list')
        


