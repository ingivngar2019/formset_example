from django.shortcuts import render, redirect

# Create your views here.

from .forms import BookFormset
from .models import Book

from .models import *
from .forms import BookForm, BookFormset,  AddableBookFormset
from django.forms import formset_factory, BaseFormSet


def create_book_normal(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Dynamic Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                genre = form.cleaned_data.get('genre')
                print(genre)
                # save book instance
                if name:
                    Book(name=name, genre=genre).save()
            # once all books are saved, redirect to book list view
            return redirect('example')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


def create_book_fixed(request):
    template_name = 'store/create_fixed.html'
    heading_message = 'Fixed Formset Demo'
    generos = Genre.objects.all()
    # INICIO DEL METODO GET
    if request.method == 'GET':
        # MAKE FORMSET
        myBookformset = formset_factory(BookForm, extra=0)
        # INITIAL FORM IN FORMSET
        formset = myBookformset(initial=[{
            'name': 'Libro de ' + x.desc ,
            # 'genre': x,
            'genero': x.id}
            for x in generos
        ])

    # FIND EL METODO GET
    elif request.method == 'POST':
        myBookformset = formset_factory(BookForm, extra=0)
        formset = myBookformset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # se obtiene el genero con base al valor hidden del template (id)
                genre = Genre.objects.get(id=form.cleaned_data.get('genero'))

                # save book instance
                if name:
                    Book(name=name, genre=genre).save()
            # once all books are saved, redirect to book list view
            return redirect('/secrets/books/book/')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
        'generos':generos
    })
